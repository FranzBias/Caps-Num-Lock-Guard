# 🔠🔢 Caps & Num Lock Guard

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![Made with love](https://img.shields.io/badge/made%20with-%E2%9D%A4%EF%B8%8F%20by%20Francesco-blueviolet)
[![GitLab mirror](https://img.shields.io/badge/mirror-GitLab-FC6D26?logo=gitlab&logoColor=white)](https://gitlab.com/FranzBias/Caps-Num-Lock-Guard)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/platform-Linux%20(X11)-lightgrey)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
[![Donate](https://img.shields.io/badge/Donate-PayPal-00457C?logo=paypal)](https://www.paypal.com/donate/?hosted_button_id=HUF5MYDG465RY)

**🌍 Languages:**
[English](#english) ·
[Italiano](#italiano) ·
[Deutsch](#deutsch) ·
[Español](#espanol) ·
[Français](#francais) ·
[Nederlands](#nederlands) ·
[Русский](#russkij) ·
[العربية](#arabic) ·
[中文](#chinese) ·
[日本語](#japanese)

---

<a id="english"></a>
## 🇬🇧 English

### What it does
A tiny background guard for the two lock keys of your keyboard:
- 🔠 **Caps Lock** — switched off after a few seconds (10 by default) or as soon as you move to another window, whichever comes first. No more MESSAGES THAT SHOUT by mistake.
- 🔢 **Num Lock** — kept the way you want: **always on** (default), **always off**, or left alone. If you change it on purpose, the guard waits until you stop typing (5 seconds by default) and then restores it. The mouse does not count as typing.

### Settings
Everything lives in `~/.config/caps-num-lock-guard/config.ini`, created on the first run and commented line by line. **Save the file and the guard picks up the changes by itself** — no restart. A wrong value (say, `timeout_seconds = lots`) does not crash it: it prints a warning and uses the defaults.

```ini
[caps_lock]
enabled = true
timeout_seconds = 10
off_on_window_change = true

[num_lock]
mode = always_on        # always_on | always_off | ignore
idle_seconds = 5

[general]
poll_interval = 0.5
```

### Requirements
Linux with **X11** (Cinnamon, MATE, Xfce…), Python 3.10+, and `xset`, `xdotool`, `xinput`. Optional but recommended: `numlockx`.
```bash
sudo apt install x11-xserver-utils xdotool xinput numlockx
```
> ⚠️ Wayland is not supported: `xset` and `xdotool` cannot read or press keys there.

### Installation
1. Copy `caps-num-lock-guard.py` to a folder of your choice, e.g. `~/.local/bin/`.
2. Create `~/.config/autostart/caps-num-lock-guard.desktop`:
   ```ini
   [Desktop Entry]
   Type=Application
   Name=Caps & Num Lock Guard
   Exec=python3 /home/YOUR-USER/.local/bin/caps-num-lock-guard.py
   X-GNOME-Autostart-Delay=11
   ```
3. Log out and back in (or start the script by hand once).

Useful options: `--write-config` creates the default settings file, and `--show-config` prints the settings currently in use.

### How it works
LED states come from `xset q`, the active window from `xdotool getactivewindow`, and keyboard activity from `xinput test-xi2 --root` (key presses only). Num Lock is set with `numlockx`, never toggled blindly. The guard also ignores the key presses it makes itself, so it does not take its own shadow for you typing.

---

<a id="italiano"></a>
## 🇮🇹 Italiano

### Cosa fa
Un piccolo guardiano, sempre in sottofondo, dei due tasti di blocco della tastiera:
- 🔠 **Caps Lock**: spento dopo pochi secondi (10 di base) oppure appena cambi finestra, a seconda di cosa arriva prima. Basta MESSAGGI CHE URLANO per sbaglio.
- 🔢 **Bloc Num**: resta come lo vuoi tu, **sempre acceso** (di base), **sempre spento** o lasciato stare. Se lo cambi apposta, il guardiano aspetta che smetti di scrivere (5 secondi di base) e poi lo rimette a posto. Il mouse non conta come scrittura.

### Impostazioni
Tutto sta in `~/.config/caps-num-lock-guard/config.ini`, creato al primo avvio e commentato riga per riga. **Salvi il file e il guardiano se ne accorge da solo**, senza riavvii. Un valore sbagliato (per esempio `timeout_seconds = tanto`) non lo fa cadere: avvisa e usa i valori predefiniti.

### Requisiti
Linux con **X11** (Cinnamon, MATE, Xfce…), Python 3.10+, `xset`, `xdotool` e `xinput`; consigliato `numlockx`.
`sudo apt install x11-xserver-utils xdotool xinput numlockx`
> ⚠️ Wayland non è supportato.

### Installazione
1. Copia `caps-num-lock-guard.py` dove preferisci, per esempio `~/.local/bin/`.
2. Crea `~/.config/autostart/caps-num-lock-guard.desktop` come nell'esempio inglese qui sopra, con il tuo percorso in `Exec=`.
3. Esci e rientra nella sessione, oppure avvia lo script a mano la prima volta.

Opzioni utili: `--write-config` crea il file delle impostazioni, `--show-config` mostra quelle in uso.

---

<a id="deutsch"></a>
## 🇩🇪 Deutsch

### Was es macht
Ein kleiner Wächter im Hintergrund für die zwei Feststelltasten:
- 🔠 **Feststelltaste (Caps Lock)**: wird nach wenigen Sekunden (Standard 10) ausgeschaltet oder sobald du das Fenster wechselst, je nachdem, was zuerst eintritt. Keine NACHRICHTEN MEHR, DIE AUS VERSEHEN SCHREIEN.
- 🔢 **Num-Taste (Num Lock)**: bleibt, wie du sie willst, nämlich **immer an** (Standard), **immer aus** oder unberührt. Änderst du sie absichtlich, wartet der Wächter, bis du aufhörst zu tippen (Standard 5 Sekunden), und stellt sie dann wieder her. Die Maus zählt nicht als Tippen.

### Einstellungen
Alles steht in `~/.config/caps-num-lock-guard/config.ini`, das beim ersten Start angelegt und Zeile für Zeile kommentiert wird. **Datei speichern, und der Wächter übernimmt die Änderungen von selbst**, ganz ohne Neustart. Ein falscher Wert bringt ihn nicht zum Absturz: Er warnt und nimmt die Standardwerte.

### Voraussetzungen
Linux mit **X11**, Python 3.10+, `xset`, `xdotool`, `xinput`; empfohlen `numlockx`.
`sudo apt install x11-xserver-utils xdotool xinput numlockx`. ⚠️ Wayland wird nicht unterstützt.

### Installation
Skript z. B. nach `~/.local/bin/` kopieren, eine Autostart-Datei `~/.config/autostart/caps-num-lock-guard.desktop` wie im englischen Beispiel anlegen, ab- und wieder anmelden. Optionen: `--write-config`, `--show-config`.

---

<a id="espanol"></a>
## 🇪🇸 Español

### Qué hace
Un pequeño guardián en segundo plano para las dos teclas de bloqueo:
- 🔠 **Bloq Mayús (Caps Lock)**: se apaga tras unos segundos (10 por defecto) o al cambiar de ventana, lo que ocurra primero.
- 🔢 **Bloq Num (Num Lock)**: se queda como tú quieras, **siempre encendido** (por defecto), **siempre apagado** o sin tocar. Si lo cambias a propósito, el guardián espera a que dejes de escribir (5 s) y lo restablece.

### Ajustes
En `~/.config/caps-num-lock-guard/config.ini`, comentado línea a línea: **guardas el archivo y el guardián aplica los cambios solo**. Un valor erróneo no lo rompe: avisa y usa los valores por defecto.

### Requisitos e instalación
Linux con **X11**, Python 3.10+, `xset`, `xdotool`, `xinput` (y `numlockx`, recomendado). ⚠️ Wayland no está soportado. Copia el script, crea `~/.config/autostart/caps-num-lock-guard.desktop` como en el ejemplo en inglés y vuelve a iniciar sesión. Opciones: `--write-config`, `--show-config`.

---

<a id="francais"></a>
## 🇫🇷 Français

### Ce qu'il fait
Un petit gardien en arrière-plan pour les deux touches de verrouillage :
- 🔠 **Verr. Maj (Caps Lock)** : désactivée après quelques secondes (10 par défaut) ou dès que vous changez de fenêtre, selon ce qui arrive en premier.
- 🔢 **Verr. Num (Num Lock)** : reste comme vous le souhaitez, c'est-à-dire **toujours activé** (par défaut), **toujours désactivé** ou laissé tranquille. Si vous la changez exprès, le gardien attend que vous arrêtiez de taper (5 s) puis la rétablit.

### Réglages
Dans `~/.config/caps-num-lock-guard/config.ini`, commenté ligne par ligne : **enregistrez le fichier, le gardien prend les changements tout seul**. Une valeur erronée ne le fait pas planter : il prévient et reprend les valeurs par défaut.

### Prérequis et installation
Linux avec **X11**, Python 3.10+, `xset`, `xdotool`, `xinput` (`numlockx` recommandé). ⚠️ Wayland n'est pas pris en charge. Copiez le script, créez `~/.config/autostart/caps-num-lock-guard.desktop` comme dans l'exemple anglais, puis reconnectez-vous. Options : `--write-config`, `--show-config`.

---

<a id="nederlands"></a>
## 🇳🇱 Nederlands

### Wat het doet
Een kleine bewaker op de achtergrond voor de twee vergrendeltoetsen:
- 🔠 **Caps Lock**: gaat uit na een paar seconden (standaard 10) of zodra je van venster wisselt, wat het eerst gebeurt.
- 🔢 **Num Lock**: blijft zoals jij wilt, namelijk **altijd aan** (standaard), **altijd uit** of ongemoeid. Verander je hem bewust, dan wacht de bewaker tot je stopt met typen (5 s) en zet hem dan terug.

### Instellingen
In `~/.config/caps-num-lock-guard/config.ini`, regel voor regel toegelicht: **sla het bestand op en de bewaker neemt de wijzigingen vanzelf over**. Een foute waarde laat hem niet crashen: hij waarschuwt en gebruikt de standaardwaarden.

### Vereisten en installatie
Linux met **X11**, Python 3.10+, `xset`, `xdotool`, `xinput` (`numlockx` aanbevolen). ⚠️ Wayland wordt niet ondersteund. Kopieer het script, maak `~/.config/autostart/caps-num-lock-guard.desktop` zoals in het Engelse voorbeeld en log opnieuw in. Opties: `--write-config`, `--show-config`.

---

<a id="russkij"></a>
## 🇷🇺 Русский

### Что делает
Маленький фоновый страж для двух клавиш-переключателей:
- 🔠 **Caps Lock** выключается через несколько секунд (по умолчанию 10) или сразу при смене окна — что наступит раньше.
- 🔢 **Num Lock** остаётся таким, как вы хотите: **всегда включён** (по умолчанию), **всегда выключен** или без изменений. Если вы переключили его намеренно, страж ждёт, пока вы перестанете печатать (5 с), и возвращает нужное состояние.

### Настройки
Файл `~/.config/caps-num-lock-guard/config.ini` с комментариями к каждой строке: **сохраните файл — страж сам применит изменения**. Ошибочное значение не приводит к сбою: появится предупреждение и будут использованы значения по умолчанию.

### Требования и установка
Linux с **X11**, Python 3.10+, `xset`, `xdotool`, `xinput` (рекомендуется `numlockx`). ⚠️ Wayland не поддерживается. Скопируйте скрипт, создайте `~/.config/autostart/caps-num-lock-guard.desktop` по английскому примеру и перезайдите в сеанс. Опции: `--write-config`, `--show-config`.

---

<a id="arabic"></a>
## 🇸🇦 العربية

<div dir="rtl">

### ماذا يفعل
حارس صغير يعمل في الخلفية لمفتاحي القفل في لوحة المفاتيح:
- 🔠 **Caps Lock**: يُطفأ بعد بضع ثوانٍ (10 افتراضيًا) أو فور الانتقال إلى نافذة أخرى، أيهما أسبق.
- 🔢 **Num Lock**: يبقى كما تريد: **مُشغَّلًا دائمًا** (افتراضيًا)، أو **مُطفأً دائمًا**، أو دون تدخل. إذا غيّرته عمدًا، ينتظر الحارس حتى تتوقف عن الكتابة (5 ثوانٍ) ثم يعيده.

### الإعدادات
في الملف `~/.config/caps-num-lock-guard/config.ini` مع شرح لكل سطر: **احفظ الملف وسيطبّق الحارس التغييرات تلقائيًا**. القيمة الخاطئة لا توقفه: يُنبّه ويستخدم القيم الافتراضية.

### المتطلبات والتثبيت
لينكس مع **X11**، وPython 3.10+، و`xset` و`xdotool` و`xinput` (ويُنصح بـ`numlockx`). ⚠️ Wayland غير مدعوم. انسخ السكربت، وأنشئ `~/.config/autostart/caps-num-lock-guard.desktop` كما في المثال الإنجليزي، ثم أعد تسجيل الدخول. الخيارات: `--write-config` و`--show-config`.

</div>

---

<a id="chinese"></a>
## 🇨🇳 中文

### 功能简介
一个在后台运行的小守护程序，专门看管键盘上的两个锁定键：
- 🔠 **Caps Lock（大写锁定）**：几秒后（默认 10 秒）或切换窗口时自动关闭，以先发生者为准。
- 🔢 **Num Lock（数字锁定）**：保持你想要的状态：**始终开启**（默认）、**始终关闭**或不予干预。如果你有意改变它，守护程序会等你停止打字（5 秒）后再恢复。

### 设置
配置文件为 `~/.config/caps-num-lock-guard/config.ini`，每行都有注释：**保存文件后，守护程序会自动应用更改**，无需重启。填错的值不会导致崩溃：程序会给出警告并使用默认值。

### 要求与安装
需要带 **X11** 的 Linux、Python 3.10+、`xset`、`xdotool`、`xinput`（推荐 `numlockx`）。⚠️ 不支持 Wayland。复制脚本，按英文示例创建 `~/.config/autostart/caps-num-lock-guard.desktop`，然后重新登录。选项：`--write-config`、`--show-config`。

---

<a id="japanese"></a>
## 🇯🇵 日本語

### できること
キーボードの 2 つのロックキーを見張る、小さな常駐プログラムです。
- 🔠 **Caps Lock**：数秒後（既定は 10 秒）、またはウィンドウを切り替えた時点で、早いほうに合わせて自動でオフにします。
- 🔢 **Num Lock**：お好みの状態を保ちます。選べるのは **常にオン**（既定）、**常にオフ**、または干渉しない、の 3 つ。意図的に切り替えた場合は、入力が止まってから（5 秒）元に戻します。

### 設定
`~/.config/caps-num-lock-guard/config.ini` に 1 行ずつ説明付きで書かれています。**ファイルを保存するだけで変更が自動的に反映されます**（再起動不要）。値を間違えても停止せず、警告を出して既定値を使います。

### 必要なものとインストール
**X11** の Linux、Python 3.10 以上、`xset`・`xdotool`・`xinput`（`numlockx` 推奨）。⚠️ Wayland には対応していません。スクリプトをコピーし、英語の例にならって `~/.config/autostart/caps-num-lock-guard.desktop` を作成し、再ログインしてください。オプション：`--write-config`、`--show-config`。

---

## Credits
- Original idea and script: Francesco (FranzBias), 2026. Written with Aldus 🦉.
- No third-party code. Tools used: [xdotool](https://github.com/jordansissel/xdotool), [numlockx](https://github.com/rg3/numlockx), `xset` and `xinput` from X.Org.

*Version 1.0.0 · MIT License*
