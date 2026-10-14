# OpenCode - Commandes principales

## Démarrage

```bash
# Lance l'interface OpenCode dans le répertoire courant
opencode

# Lance OpenCode dans un projet spécifique
opencode /chemin/vers/projet

# Reprend la dernière session
opencode --continue

# Reprend une session donnée
opencode --session <session-id>

# Reprend une session en créant une branche de travail séparée
opencode --session <session-id> --fork

# Démarre avec un modèle spécifique
opencode --model ollama/qwen3:8b

# Démarre avec un prompt initial
opencode --prompt "Analyse ce projet Spring Boot"

# Auto-approuve les actions autorisées
opencode --auto
```

---

## Exécution ponctuelle

```bash
# Exécute une requête sans ouvrir l'interface interactive
opencode run "Explique-moi cette classe Java"

# Analyse un projet
opencode run "Analyse cette application Spring Boot"

# Génère des tests
opencode run "Génère les tests unitaires manquants"

# Revue de code
opencode run "Fais une revue de code du projet"
```

---

## Authentification des fournisseurs IA

```bash
# Connexion à un fournisseur (OpenAI, Anthropic, Gemini, Mistral, OpenRouter, ...)
opencode auth login

# Liste les fournisseurs configurés
opencode auth list

# Déconnecte un fournisseur
opencode auth logout
```

---

## Modèles IA

```bash
# Liste tous les modèles disponibles
opencode models

# Liste les modèles d'un fournisseur
opencode models openai

# Rafraîchit le catalogue
opencode models --refresh
```

---

## Agents

```bash
# Liste les agents disponibles
opencode agent list

# Crée un nouvel agent interactif
opencode agent create

# Création non interactive
opencode agent create \
  --description "Expert Spring Boot" \
  --mode primary \
  --permissions all
```

### Cas d'usage d'agents

- Expert Spring Boot
- Expert GitLab CI/CD
- Expert SonarQube
- Expert Kubernetes
- Reviewer Java
- Générateur de tests

---

## Sessions

```bash
# Liste les sessions
opencode session list

# Supprime une session
opencode session delete <session-id>

# Exporte une session
opencode export <session-id>

# Importe une session
opencode import session.json
```

---

## Statistiques

```bash
# Affiche les coûts, tokens consommés et statistiques
opencode stats
```

---

## MCP (Model Context Protocol)

```bash
# Liste les serveurs MCP
opencode mcp list

# Ajoute un serveur MCP
opencode mcp add

# Authentifie un MCP
opencode mcp auth

# Débogue un MCP
opencode mcp debug

# Déconnexion
opencode mcp logout
```

### Exemples de MCP utiles

- GitLab
- GitHub
- Jira
- Confluence
- SonarQube
- Azure DevOps

---

## Serveur OpenCode

```bash
# Démarre uniquement l'API serveur
opencode serve

# Lance l'interface Web
opencode web

# Interface Web sur un port spécifique
opencode web --port 4096

# Écoute sur toutes les interfaces réseau
opencode web --hostname 0.0.0.0 --port 4096
```

---

## Connexion à un serveur distant

```bash
# Attache un client TUI à un serveur OpenCode
opencode attach http://localhost:4096

# Avec authentification
opencode attach http://10.20.30.40:4096 \
  --username opencode \
  --password secret
```

---

## ACP (Agent Client Protocol)

```bash
# Démarre le bridge ACP pour IDE
opencode acp
```

Permet l'intégration avec les IDE compatibles ACP.

---

## GitHub

```bash
# Installe ou configure l'agent GitHub
opencode github

# Analyse une Pull Request
opencode pr 123
```

---

## Plugins

```bash
# Installe un plugin
opencode plugin <nom-plugin>

# Alias
opencode plug <nom-plugin>
```

---

## Workflow quotidien (Java / Spring Boot)

```bash
# 1. Ouvrir le projet
opencode .

# 2. Demander une analyse globale
Analyse cette application Spring Boot.
Identifie les problèmes d'architecture.

# 3. Génération des tests
Génère les tests unitaires manquants.

# 4. Revue de code
Fais une revue complète du projet.

# 5. Analyse CI/CD
Analyse mon .gitlab-ci.yml et propose des améliorations.

# 6. Analyse Sonar
Identifie les problèmes qui pourraient faire échouer un Quality Gate SonarQube.

# 7. Sécurité
Analyse les vulnérabilités OWASP potentielles.
```

---

## Configuration Ollama (exemples)

```bash
# Télécharger les modèles
ollama pull qwen3:8b
ollama pull deepseek-r1:8b
ollama pull gemma3:12b
ollama pull mistral-small

# Vérifier les modèles
ollama list

# Tester un modèle
ollama run qwen3:8b

# Utilisation dans OpenCode
opencode --model ollama/qwen3:8b
```

---

