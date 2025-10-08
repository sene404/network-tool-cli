#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Subnet Calculator
-----------------
Un outil en ligne de commande pour calculer les informations d’un sous-réseau :
- Adresse réseau
- Adresse de broadcast
- Plage d’adresses IP disponibles
- Nombre total d’hôtes possibles

Auteur : Sene
GitHub : https://github.com/sene404
"""

from colorama import Fore, Style, init


# Initialisation de colorama (utile sous Windows)
init(autoreset=True)


def validate_ip(ip_str: str) -> bool:
    """Vérifie si une adresse IP est valide (IPv4)."""
    parts = ip_str.split(".")
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False


def ip_to_binary(ip: str) -> str:
    """Convertit une adresse IPv4 en binaire."""
    return "".join(f"{int(octet):08b}" for octet in ip.split("."))


def binary_to_ip(binary_str: str) -> str:
    """Convertit une chaîne binaire de 32 bits en adresse IPv4."""
    return ".".join(str(int(binary_str[i:i + 8], 2)) for i in range(0, 32, 8))


def calculate_subnet(ip: str, mask: str) -> dict:
    """Calcule les informations du sous-réseau à partir d'une IP et d’un masque."""
    total_bits = 32

    ip_bin = ip_to_binary(ip)
    mask_bin = ip_to_binary(mask)
    bits_subnet = mask_bin.count("1")

    # Calcul des adresses réseau et broadcast
    network_bin = ip_bin[:bits_subnet] + "0" * (total_bits - bits_subnet)
    broadcast_bin = ip_bin[:bits_subnet] + "1" * (total_bits - bits_subnet)

    # Conversion en format décimal
    network_address = binary_to_ip(network_bin)
    broadcast_address = binary_to_ip(broadcast_bin)

    # Calcul des adresses disponibles
    first_ip_bin = network_bin[:-1] + "1"
    last_ip_bin = broadcast_bin[:-1] + "0"

    first_ip = binary_to_ip(first_ip_bin)
    last_ip = binary_to_ip(last_ip_bin)

    # Nombre d’hôtes possibles
    nb_hosts = 2 ** (total_bits - bits_subnet) - 2

    return {
        "ip": ip,
        "mask": mask,
        "cidr": bits_subnet,
        "network": network_address,
        "broadcast": broadcast_address,
        "first_ip": first_ip,
        "last_ip": last_ip,
        "nb_hosts": nb_hosts
    }


def display_results(results: dict) -> None:
    """Affiche les résultats de manière colorée et lisible."""
    print(Fore.CYAN + "\n===== Résultats du calcul =====")
    print(Fore.GREEN + f"Adresse IP saisie : {results['ip']}")
    print(Fore.GREEN + f"Masque de sous-réseau : {results['mask']} (/{results['cidr']})")
    print(Fore.YELLOW + f"Adresse réseau : {results['network']}")
    print(Fore.YELLOW + f"Adresse de broadcast : {results['broadcast']}")
    print(Fore.MAGENTA + f"Plage d'adresses utilisables : {results['first_ip']} - {results['last_ip']}")
    print(Fore.BLUE + f"Nombre d'hôtes possibles : {results['nb_hosts']}")
    print(Style.RESET_ALL)


def main():
    """Point d’entrée principal du script."""
    print(Fore.CYAN + "=== Calculateur de sous-réseau IPv4 ===" + Style.RESET_ALL)

    while True:
        ip = input("Entrez une adresse IP (ex: 192.168.1.0) : ").strip()
        mask = input("Entrez un masque de sous-réseau (ex: 255.255.255.0) : ").strip()

        if not validate_ip(ip) or not validate_ip(mask):
            print(Fore.RED + "❌ Adresse IP ou masque invalide. Veuillez réessayer.\n")
            continue

        results = calculate_subnet(ip, mask)
        display_results(results)
        break


if __name__ == "__main__":
    main()
