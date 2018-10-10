# DGA-Hunting
What's Shannon Entropy? 
"... a measure of uncertainty in a random variable"

![alt text](http://www.bearcave.com/misl/misl_tech/wavelets/compression/shannon2.jpg)

How does it help finding malware ana anomalous activity?
The more random a string is, the higher its calculation of randomness. For example:

  URL: abcdefghijklmnopqrstuvwxyz.1234567890-ADGJLPIYRWZCBM.com      
  Shannon Score: 5.6644977792

  URL: google.com
  Shannon Score: 2.64643934467

Domains and subdomains with high entropy are good indicators of malicious behavior. We can filter to domains or subdomains with a score above 3 or 4.
Cons:
- False positives.
- CDNs like Amazon, Akamai, and others use pseudorandom generated subdomains
- Malware evolves: Locky & others using shorter subdomains or domains to reduce randomness, reducing entropy score.
