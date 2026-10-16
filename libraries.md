# AI UX Lab

## Projet

Cette application est une plateforme de gestion des commandes clients.

L'application permet :

- de consulter les clients ;
- de rechercher des produits ;
- de créer une commande ;
- de modifier une commande brouillon ;
- de confirmer une commande ;
- d'annuler une commande.

## UX Principles

- Simplicité avant richesse fonctionnelle.
- Réduire le nombre d'étapes utilisateur.
- Limiter la charge cognitive.
- Fournir un feedback immédiat à chaque action.
- Prévenir les erreurs lorsque c'est possible.
- Respecter les standards d'accessibilité.

## Design

- Mobile First.
- Responsive design.
- Design System cohérent.
- Utiliser une grille 8px.
- Respecter les contrastes AA WCAG.

## Research

Avant toute proposition :

1. Identifier les utilisateurs.
2. Identifier leurs objectifs.
3. Identifier leurs frustrations possibles.
4. Décrire les scénarios d'usage.

## Deliverables

Les livrables peuvent inclure :

- Personas.
- User Journey.
- User Flow.
- Wireframes.
- Maquettes.
- Design System.
- Audit UX.
- Recommandations ergonomiques.

## Verification

Avant de considérer une tâche terminée :

1. Vérifier la cohérence du parcours.
2. Vérifier l'accessibilité.
3. Vérifier les états d'erreur.
4. Vérifier les cas limites.
5. Justifier les choix UX.

## Important

Ne pas inventer de besoins métier.

Si une règle métier est ambiguë, demander une clarification.


Exercice 1 : Découverte utilisateur


# TASK

Analyse les règles métier fournies.

Produis :

- 2 personas ;
- leurs objectifs ;
- leurs frustrations ;
- leurs principaux parcours dans l'application.


Exercice 2 : User Journey


# TASK

Construis le User Journey complet d'un client qui :

- sélectionne des produits ;
- crée une commande ;
- confirme sa commande.

Présente :

- les actions ;
- les émotions ;
- les points de friction ;
- les opportunités d'amélioration.

Exercice 3 : User Flow

# TASK

Conçois le User Flow permettant :

- la création d'une commande ;
- l'ajout de produits ;
- la confirmation de la commande ;
- l'annulation d'une commande.

Utilise une représentation textuelle ou Mermaid.


Exercice 4 : Wireframes

# TASK

Propose les wireframes basse fidélité des écrans suivants :

- Liste des commandes
- Création de commande
- Détail d'une commande
- Confirmation
- Annulation

Décris précisément :

- structure ;
- composants ;
- hiérarchie visuelle ;
- actions utilisateur.


Exercice 5 : États et erreurs

# TASK

Pour l'écran de création de commande :

identifie tous les états possibles :

- chargement ;
- vide ;
- erreur ;
- succès ;
- produit inactif ;
- quantité invalide ;
- commande confirmée ;
- commande annulée.

Propose pour chacun :

- le message ;
- le comportement du système ;
- le feedback utilisateur.

Exercice 6 : Design System

# TASK

À partir du contexte métier fourni :

propose un mini Design System contenant :

- couleurs ;
- typographie ;
- boutons ;
- champs de formulaire ;
- tableaux ;
- messages d'erreur ;
- badges de statut.

Justifie chaque choix.
``

Exercice 7 : Collaboration UX / Dev

# TASK

À partir des règles métier :

rédige des User Stories complètes :

- description ;
- critères d'acceptation ;
- cas d'erreur ;
- maquettes attendues ;
- impacts techniques éventuels.

Format :

Given / When / Then


Exercice bonus IA


Analyse BUSINESS_RULES.md

Identifie les principaux risques UX.

Propose :

- un User Flow ;
- des wireframes ;
- les composants nécessaires ;
- les états d'erreur ;
- les critères d'accessibilité.

# Exercice 8 : Analyse UX des règles métier

# TASK

Analyse BUSINESS_RULES.md.

Identifie :

- les validations utilisateur nécessaires ;
- les erreurs possibles ;
- les informations obligatoires à afficher ;
- les feedbacks attendus ;
- les risques de confusion utilisateur.

Pour chaque élément :

- citer la règle métier concernée ;
- expliquer l'impact utilisateur ;
- proposer une recommandation UX.

---

# Exercice 9 : États et comportements de l'interface

# TASK

À partir des règles métier, définis les états de l'interface pour :

- création de commande ;
- consultation ;
- confirmation ;
- annulation.

Pour chaque état :

- actions autorisées ;
- actions interdites ;
- comportement système ;
- feedback utilisateur ;
- message affiché.

Présente le résultat sous forme de tableau.

---

# Exercice 10 : UX Review des User Stories

# TASK

Analyse les User Stories produites par les développeurs.

Vérifie :

- la clarté du parcours utilisateur ;
- les validations ;
- les messages utilisateur ;
- les erreurs métier ;
- les cas limites ;
- les besoins d’accessibilité.

Pour chaque problème identifié :

- sévérité ;
- problème observé ;
- impact utilisateur ;
- recommandation.

---

# Exercice 11 : Conception à partir des API

# TASK

À partir des DTO et endpoints Spring Boot :

- identifie les écrans nécessaires ;
- identifie les composants nécessaires ;
- identifie les interactions utilisateur ;
- identifie les informations manquantes.

Justifie chaque proposition à partir de l'API observée.

---

# Exercice 12 : Gestion des transitions métier

# TASK

Analyse les transitions autorisées :

DRAFT -> CONFIRMED
DRAFT -> CANCELLED
CONFIRMED -> CANCELLED

Conçois une interface qui :

- guide l'utilisateur ;
- empêche les transitions interdites ;
- affiche clairement le statut courant ;
- fournit un feedback adapté.

Produis :

- règles UX ;
- composants ;
- états visuels ;
- messages utilisateur.

---

# Exercice 13 : Collaboration avec le Reviewer

# TASK

À partir d'un rapport produit par l'agent Reviewer :

- analyse l'impact utilisateur ;
- propose une correction UX ;
- définis les messages utilisateur ;
- définis les comportements attendus.

Pour chaque anomalie :

- description ;
- impact ;
- recommandation ;
- priorité.

---

# Exercice 14 : Collaboration avec le Tester

# TASK

Analyse les scénarios proposés par l'agent Tester.

Pour chaque scénario :

- comportement attendu ;
- message utilisateur ;
- visualisation de l'erreur ;
- gestion mobile ;
- considérations d'accessibilité.

Complète les scénarios manquants si nécessaire.

---

# Exercice 15 : Audit Accessibilité

# TASK

Réalise un audit accessibilité de l'application.

Vérifie :

- navigation clavier ;
- contraste ;
- focus ;
- lecteur d'écran ;
- messages d'erreur ;
- responsive mobile.

Classe les problèmes :

- Critique ;
- Majeur ;
- Mineur.

Pour chaque problème :

- constat ;
- impact ;
- recommandation.

---

# Exercice 16 : UX Definition of Done

# TASK

Construis une checklist UX réutilisable pour le projet.

La checklist doit couvrir :

- états de chargement ;
- états vides ;
- états d'erreur ;
- états de succès ;
- accessibilité ;
- responsive ;
- validations ;
- feedback utilisateur ;
- cohérence visuelle.

Présente le résultat sous forme de checklist.

---

# Exercice 17 : Création d'un Agent UX Reviewer

# TASK

Conçois un agent IA spécialisé UX.

L'agent devra analyser :

- les parcours utilisateur ;
- les écrans ;
- les User Stories ;
- les maquettes ;
- les comportements ;
- l'accessibilité.

Fournis :

- le prompt système complet ;
- les responsabilités de l'agent ;
- les limites ;
- le format du rapport produit.

Le rapport devra préciser :

1. Sévérité
2. Écran concerné
3. Problème
4. Impact utilisateur
5. Recommandation