str1 = """Sarah Connor
+1-202-555-0198
88 Skynet Ave., Los Angeles CA 90210
sconnor@example.com

Rajesh Kumar
+91-98201-12345
42 Nehru Road, Mumbai MH 400001
rajesh.k@mail.org

Emma Thompson
202-555-0183
120 Maple Lane, Springfield IL 62704
emma.thompson@inbox.co

Jean-Luc Picard
+33-1-44-55-66-77
18 Rue de Starfleet, Paris 75001
jl.picard@enterprise.fr

Maria Gonzalez
303-555-7890
98 Sunset Blvd, Austin TX 73301
maria.g@random.io

Takeshi Yamamoto
+81-90-1234-5678
3-12-5 Roppongi, Minato-ku Tokyo 106-0032
takeyama@data.net

Linda Grey
+91 9125553345
500 7th Ave, New York NY 10018
lgrey@workmail.com

Carlos Mendes
305-555-9988
144 Ocean Drive, Miami FL 33139
carlos.m@maildrop.cc

Jane Doe
555-123-4567
742 Evergreen Terrace, Springfield OR 97477
jane_d@example.net

Nathan Drake
+44 20 7946 0958
12 Treasure Lane, London W1D 3QJ
nathan.d@explorer.uk

Anna Schmidt
+49 89 123456
78 Berliner Str., Munich 80331
aschmidt@randommail.de

Michael Zhao
647-555-2376
89 King St. W, Toronto ON M5H 1J9
m.zhao@mail.ca

Fatima Noor
050-123-4567
23 Palm Rd., Dubai, UAE
fnoor@emirates.net """

import re

phone = re.compile(r"\+91[-\s]?\d{5}-?\d{5}")
domain = re.compile(r"\.\w{2,}")
names = re.compile(r"[a-zA-Z-]+ [a-zA-Z]+")

matches1 = re.findall(phone, str1)
matches2 = re.findall(domain,str1) #wrong
matches3 = re.findall(names,str1)
print(matches1)
print(matches2)
print(matches3)