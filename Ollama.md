# Ollama - Commandes principales

## Installation

### Vérifier l'installation

```bash
ollama --version
```

Affiche la version installée.

---

## Gestion des modèles

### Télécharger un modèle

```bash
ollama pull qwen3:8b
ollama pull deepseek-r1:8b
ollama pull gemma3:12b
ollama pull mistral-small
ollama pull llama3.3
```

Télécharge le modèle localement.

---

### Lister les modèles installés

```bash
ollama list
```

Exemple :

```text
NAME             ID          SIZE
qwen3:8b         xxxxxxxx    5.2 GB
gemma3:12b       yyyyyyyy    8.1 GB
deepseek-r1:8b   zzzzzzzz    5.0 GB
```

---

### Afficher les détails d'un modèle

```bash
ollama show qwen3:8b
```

Informations :

- paramètres
- taille
- quantification
- prompt système

---

### Supprimer un modèle

```bash
ollama rm qwen3:8b
```

Libère de l'espace disque.

---

### Copier un modèle

```bash
ollama cp qwen3:8b qwen3-custom
```

Permet de créer un dérivé personnalisé.

---

## Exécution

### Démarrer un modèle

```bash
ollama run qwen3:8b
```

Ouvre un chat interactif.

---

### Exécuter directement un prompt

```bash
ollama run qwen3:8b "Explique Spring Security"
```

---

### Mode conversation

```bash
ollama run gemma3:12b
```

Puis :

```text
>>> Explique-moi Docker.
>>> Quels sont les avantages de Kubernetes ?
```

---

### Quitter la conversation

```text
/bye
```

ou

```text
Ctrl + D
```

---

## Modèles actuellement chargés

### Voir les modèles en mémoire

```bash
ollama ps
```

Exemple :

```text
NAME           SIZE     PROCESSOR