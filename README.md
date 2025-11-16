# Kanye Says... (Desktopová Aplikácia)

Jednoduchá desktopová aplikácia vytvorená v Pythone a `tkinter`, ktorá zobrazuje náhodné citáty od Kanye Westa. Citáty sú získavané naživo z verejného API (https://api.kanye.rest).

![Ukážka Aplikácie](demo.png)
*(Odporúčame sem vložiť screenshot fungujúcej aplikácie)*

##  Ako spustiť projekt

Na spustenie aplikácie potrebujete Python 3 a niekoľko súborov.

### 1. Požiadavky

* Python 3.x
* Knižnica `tkinter` (zvyčajne je súčasťou štandardnej inštalácie Pythonu)
* Knižnica `requests`

### 2. Inštalácia

1.  Naklonujte si tento repozitár (alebo si stiahnite súbory).
2.  Nainštalujte potrebnú `requests` knižnicu:
    ```bash
    pip install requests
    ```
3.  Uistite sa, že v rovnakom adresári, kde sa nachádza váš `.py` skript, máte aj tieto súbory:
    * `background.png` (Obrázok pre pozadie textu)
    * `kanye.png` (Obrázok pre tlačidlo)

4.  Spustite skript (za predpokladu, že ste ho uložili ako `app.py`):
    ```bash
    python app.py
    ```

## 🛠️ Ako to funguje

Aplikácia sa skladá z troch hlavných častí:

1.  **GUI (Grafické rozhranie):**
    * Vytvorené pomocou knižnice `tkinter`.
    * Hlavné okno obsahuje `Canvas` (plátno), na ktorom je zobrazený obrázok pozadia (`background.png`) a text citátu.
    * Pod plátnom je `Button` (tlačidlo) s obrázkom Kanyeho (`kanye.png`).

2.  **Získanie citátu (Funkcia `get_quote`):**
    * Keď používateľ klikne na tlačidlo, spustí sa táto funkcia.
    * Odošle HTTP GET požiadavku na API `https://api.kanye.rest` pomocou knižnice `requests`.
    * Spracuje odpoveď (JSON) a vyberie z nej text citátu (`data["quote"]`).

3.  **Aktualizácia textu:**
    * Získaný citát sa následne dynamicky zobrazí na plátne pomocou metódy `canvas.itemconfig()`, ktorá prepíše pôvodný text.
