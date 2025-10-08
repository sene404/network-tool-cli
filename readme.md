# 🧮 Subnet Calculator CLI

Un outil simple et élégant en ligne de commande pour calculer les informations essentielles d’un sous-réseau IPv4.
Développé en **Python 3**, il permet d’obtenir rapidement l’adresse réseau, l’adresse de broadcast, la plage IP disponible et le nombre d’hôtes possibles.

---

## 🚀 Fonctionnalités

* Vérification automatique des adresses IP et masques
* Conversion en binaire pour calcul précis
* Affichage coloré grâce à **Colorama**
* Calcul de :

  * Adresse réseau
  * Adresse de broadcast
  * Plage d’adresses disponibles
  * Nombre d’hôtes possibles
  * CIDR (notation /xx)

---

## 🧰 Prérequis

* Python **3.8+**
* Bibliothèque [`colorama`](https://pypi.org/project/colorama/)

Installation de la dépendance :

```bash
pip install colorama
```

---

## ⚙️ Utilisation

Clonez le dépôt :

```bash
git clone https://github.com/<ton-pseudo>/subnet-calculator-cli.git
cd subnet-calculator-cli
```

Lancez le script :

```bash
python subnet_calculator.py
```

### Exemple d’exécution :

```
=== Calculateur de sous-réseau IPv4 ===
Entrez une adresse IP (ex: 192.168.1.0) : 192.168.10.0
Entrez un masque de sous-réseau (ex: 255.255.255.0) : 255.255.255.0

===== Résultats du calcul =====
Adresse IP saisie : 192.168.10.0
Masque de sous-réseau : 255.255.255.0 (/24)
Adresse réseau : 192.168.10.0
Adresse de broadcast : 192.168.10.255
Plage d'adresses utilisables : 192.168.10.1 - 192.168.10.254
Nombre d'hôtes possibles : 254
```

---

## 🧩 Structure du projet

```
📁 subnet-calculator-cli
 ┣ 📜 subnet_calculator.py
 ┣ 📜 README.md
 ┗ 📜 requirements.txt
```

---

## 🧑‍💻 Auteur

**Ton Nom**
🐙 [Ton GitHub](https://github.com/sene404)

---

## 📄 Licence

Ce projet est sous licence **MIT** — vous êtes libre de le réutiliser et le modifier.
