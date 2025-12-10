1.  (Для устранения `𐒌(1)`, `𐒌(2)`, `𐒌(4)`, `𐒌(5)`) Заменить пункт 3.1 (включая подпункты 3.1.1–3.1.7) на следующий текст:

<!-- end list -->

```markdown
3.1) Step-by-step instructions.
3.1.1) In `BC`, navigate to the «Report Layout Selection» (`RLS`) page and locate the required report.
3.1.2) Note: This method only works with Word layouts; if the report currently uses an RDLC layout, this method cannot be applied directly.
3.1.3) Choose the «Custom Layouts» action (often found under the «Process» or «Actions» menu) to open the «Custom Report Layouts» page.
3.1.4) Create a new custom Word layout (`L`) based on an existing layout, as built-in layouts cannot be modified.
3.1.5) Choose the «New» action.
3.1.6) In the dialog, ensure the «Insert Word Layout» toggle is activated and choose «OK» to create a copy of the built-in Word layout.
3.1.7) Select the newly created layout `L` and choose the «Layout» → «Export Layout» action to save it as a `.docx` file (`F`).
3.1.8) Open `F` in Microsoft Word (`W`).
3.1.9) Apply `CG` to the necessary text fields and content controls.
3.1.10) In `W`, navigate to «File» → «Options» → «Save».
3.1.11) In the section «Preserve fidelity when sharing this document», configure the following settings.
3.1.12) The «Embed fonts in the file» option must be activated.
3.1.13) To optimize the file size, it is highly recommended to activate the «Embed only the characters used in the document (best for reducing file size)» option.
3.1.14) Crucially, the «Do not embed common system fonts» option must be deactivated.
This is necessary because the `BC` SaaS server-side component often fails to correctly render custom fonts if this option is activated.
3.1.15) Save `F`.
3.1.16) Return to the «Custom Report Layouts» page in `BC`.
3.1.17) Select `L` and choose the «Layout» → «Import Layout» action to upload the modified file `F`.
3.1.18) Return to the `RLS` page.
3.1.19) For the report, set the «Selected Layout» field to «Custom Layout».
3.1.20) In the «Custom Layout Description» field, select the layout `L`.
```

2.  (Для устранения `𐒌(7)`) Заменить пункт 3.2.3 на следующий текст:

<!-- end list -->

```markdown
3.2.3) If the font is not embedded in the `.docx` file, this component reads the font name, tries to find it in the list of fonts installed on the server, does not find it, and replaces it with a default fallback font (specifically Calibri, according to Microsoft documentation), which leads to your problem.
```

3.  (Для устранения `𐒌(8)`, `𐒌(9)`) Заменить пункт 3.3 на следующий текст:

<!-- end list -->

```markdown
3.3) For the implementation of Method #1, it is important that the font's «Font Embeddability» property has the value «Editable» or «Installable».
I have checked — for `CG` this is indeed the case (it is «Installable»): see the attached file `Century Gothic.png`.
```

4.  (Для устранения `𐒌(11)`) В пункте 4 заменить предложение:

<!-- end list -->

```markdown
Unlike the native workaround, font embedding in ForNAV is a core, documented feature.
```

на предложение:

```markdown
Unlike the standard approach utilizing Microsoft Word's embedding feature, font embedding in ForNAV is a core, documented feature of the extension itself.
```