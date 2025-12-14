# Daily Cats Fact

Pushed, Built, Tested, Scanned (security) with Github Actions


Etapes : 

- [x] Lorsque l'app est push sur ma branche features, ce qui suit est triggered :
- [ ] Le container se crée -> Oui, mais encore sous le runner Ubuntu
- [x] Le code dans ce container soit executé 
- [x] Le code a été correctement executé, et voir le resultat si possible
- [x] Tester si des failles de sécurité existe dans : 
    - [x] mon Dockerfile, -> OK, semgrep
    - [x] mon container, -> OK, trivy
    - [x] mon appli python -> OK, semgrep

Si tout cela est OK, alors :
- [x] Pull request sur main, mais me laisser merge manuellement (check humain)
- [x] Push l'app sur le docker hub


Une fois tout cela OK : 
- [ ] Déployer sur AWS -> Etape suivante, apres passage du runner vers container


Ameliorations : 
- [x] Passage à une application web avec Flask + JS