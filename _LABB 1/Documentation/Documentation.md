# Dokumentera i en markdown de olika skripten och dess funktionalitet i backenden.

---

- ### **change_name_data.py**
>![change_name_data](images/image-1.png)


change_name_data.py ändrar namnet på tidigare raw_data mappen från långa namn till kortare mera lätt arbetliga namn såsom "Datum XX_XX_XXXX" till den första meningen i varje mappen med split()[0], alltså "Datum XX_XX_XXXX" -> "Datum" sedan skapar cleaned data mappen om den redan existerar tar den bort den nuvarande bearbetande datan och gör ingen förändring. (tror du hörde diskussionen med Milton om hur man kunde göra det annorlunda.)

---

- ### **constants.py**
>![constants](images/image-2.png)

constants.py vår path till youtube_data och cleaned data tillkallas som DATABASE_PATH och CLEANED_DATA_PATH senare i skripten.

---

- ### **database.py**
>![database](images/image-3.png)

database.py öppnar en connection till vår databas.

---

- ### **ingest_data_to_database.py**
>![ingest_data_to_database](images/image-4.png)

ingest_data_to_database.py

---

- ### **EDA.sql**
>![EDA](images/image-5.png)

EDA.sql

---

- ### **marts_content.sql**
>![alt text](image-6.png)

marts_content.sql

---

- ### **marts_device.sql**
>![alt text](image-7.png)

marts_device.sql

---