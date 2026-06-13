senyawa_data = {
    # ─────────────────────────────────────────────────────────────────
    # Seluruh data telah diverifikasi ulang berdasarkan MSDS standar:
    # Sigma-Aldrich, Fisher Scientific, NIOSH, GHS/SDS (ISO 11014)
    # Simbol bahaya mengacu pada piktogram GHS (Globally Harmonized System)
    # ─────────────────────────────────────────────────────────────────

    # ── ASAM-ASAM KUAT & LEMAH ────────────────────────────────────────
    "Asam Sulfat": {
        "rumus": "H₂SO₄",
        "simbol_bahaya": "Korosif | Beracun",
        # GHS: GHS05 (korosif), GHS07 (iritasi/toksik akut cat.4)
        "wujud": "Cairan kental, tidak berwarna",
        "bau": "Tidak berbau (pekat); bau menyengat jika dipanaskan",
        # MSDS: odorless liquid; pungent odor when heated (NIOSH)
        "reaktivitas": (
            "Oksidator kuat dan dehidrator; bereaksi sangat eksotermis dengan air "
            "(JANGAN tuangkan air ke asam — selalu asam ke air); "
            "bereaksi hebat dengan logam aktif (Fe, Zn, Al) menghasilkan gas H₂; "
            "bereaksi dengan basa membentuk garam sulfat (netralisasi eksotermis); "
            "mengkarbonasi senyawa organik (efek dehidrasi); "
            "bereaksi hebat dengan agen pereduksi kuat dan bahan organik mudah terbakar"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah dalam wadah tahan asam (kaca borosilikat atau plastik HDPE), "
            "beri label 'LIMBAH B3 – ASAM KUAT'.\n"
            "Langkah 2: Netralisasi perlahan dengan Na₂CO₃ padat atau larutan NaOH 10% sambil diaduk "
            "dan didinginkan hingga pH 6–8. JANGAN tambahkan air langsung ke asam pekat.\n"
            "Langkah 3: Verifikasi pH dengan indikator universal.\n"
            "Langkah 4: Encerkan filtrat dengan air (perbandingan ≥1:10).\n"
            "Langkah 5: Serahkan ke pengelola limbah B3 bersertifikat atau buang ke saluran khusus B3 "
            "sesuai izin lingkungan setempat."
        ),
    },
    "Asam Klorida": {
        "rumus": "HCl",
        "simbol_bahaya": "Korosif | Beracun",
        # GHS: GHS05 (korosif), GHS07 (iritasi akut)
        "wujud": "Cairan tidak berwarna hingga kuning pucat",
        "bau": "Menyengat kuat (gas HCl); fumes asam klorida",
        "reaktivitas": (
            "Asam kuat; bereaksi dengan logam aktif (Zn, Fe, Mg, Al) menghasilkan gas H₂; "
            "bereaksi hebat dengan basa kuat (NaOH, KOH) secara eksotermis; "
            "bereaksi dengan oksidator kuat (KMnO₄, MnO₂) menghasilkan gas Cl₂ toksik; "
            "mengeluarkan fumes HCl yang mengiritasi saluran pernapasan; "
            "korosif terhadap sebagian besar logam dan jaringan hidup"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah dalam wadah tahan asam (kaca atau plastik HDPE), "
            "beri label 'LIMBAH B3 – ASAM KUAT'.\n"
            "Langkah 2: Di lemari asam, netralisasi perlahan dengan larutan NaOH 10% atau "
            "Na₂CO₃ padat sambil diaduk hingga pH 6–8.\n"
            "Langkah 3: Verifikasi pH dengan kertas indikator universal.\n"
            "Langkah 4: Encerkan dengan air mengalir (≥1:10).\n"
            "Langkah 5: Buang ke saluran pembuangan khusus B3 atau serahkan ke pengelola "
            "limbah B3 bersertifikat."
        ),
    },
    "Asam Nitrat": {
        "rumus": "HNO₃",
        "simbol_bahaya": "Oksidator | Korosif | Beracun",
        # GHS: GHS03 (oksidator), GHS05 (korosif), GHS07 (iritasi)
        "wujud": "Cairan tidak berwarna hingga kuning pucat (karena dekomposisi → NO₂)",
        "bau": "Menyengat kuat; bau gas NO₂ (coklat-kemerahan) jika terurai",
        "reaktivitas": (
            "Oksidator kuat; bereaksi dengan logam (Cu, Ag, Pb) menghasilkan gas NOₓ toksik; "
            "bereaksi hebat dengan bahan organik (kertas, kayu, etanol) — risiko kebakaran; "
            "bereaksi dengan basa membentuk garam nitrat (netralisasi eksotermis); "
            "campuran dengan HCl membentuk aqua regia (melarutkan emas/platina); "
            "dapat meledak jika dicampur dengan bahan pereduksi atau pelarut organik; "
            "terurai pada suhu >50°C melepaskan NOₓ dan O₂"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah dalam wadah kaca atau HDPE berlabel "
            "'LIMBAH B3 – ASAM OKSIDATOR'. JANGAN campur dengan bahan organik atau pereduksi.\n"
            "Langkah 2: Di lemari asam berventilasi, netralisasi PERLAHAN dengan NaOH 10% "
            "sambil diaduk; hindari reaksi berlebihan.\n"
            "Langkah 3: Verifikasi pH 6–8 dengan indikator universal.\n"
            "Langkah 4: Encerkan ≥1:10 dengan air.\n"
            "Langkah 5: Serahkan ke pengelola limbah B3 bersertifikat — jangan dibuang "
            "langsung ke saluran umum tanpa pengolahan."
        ),
    },
    "Asam Fosfat": {
        "rumus": "H₃PO₄",
        "simbol_bahaya": "Korosif | Iritasi",
        # GHS: GHS05 (korosif pada logam/kulit), GHS07 (iritasi kulit/mata)
        "wujud": "Cairan kental tidak berwarna hingga kuning muda (bentuk cair); "
                 "atau padatan higroskopis (bentuk padat 100%)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Asam triprotik (netralisasi 3 tahap dengan basa); "
            "korosif terhadap logam aktif (Fe, Zn, Al) menghasilkan gas H₂; "
            "bereaksi dengan Ca²⁺ membentuk endapan tidak larut Ca₃(PO₄)₂; "
            "bereaksi eksotermis dengan basa kuat; "
            "tidak mudah terbakar; stabil dalam kondisi normal"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah dalam wadah tahan asam (kaca atau HDPE), "
            "beri label 'LIMBAH B3 – ASAM'.\n"
            "Langkah 2: Netralisasi perlahan dengan NaOH 10% atau Na₂CO₃ sambil diaduk "
            "hingga pH 6–8.\n"
            "Langkah 3: Verifikasi pH dengan indikator universal.\n"
            "Langkah 4: Encerkan dengan air (≥1:10).\n"
            "Langkah 5: Buang ke saluran pembuangan khusus B3 atau serahkan ke pengelola "
            "limbah B3 bersertifikat."
        ),
    },
    "Asam Asetat": {
        "rumus": "CH₃COOH",
        "simbol_bahaya": "Korosif | Mudah Terbakar",
        # GHS: GHS02 (mudah terbakar, asam glasial), GHS05 (korosif)
        "wujud": "Cairan tidak berwarna",
        "bau": "Menyengat, seperti cuka pekat",
        "reaktivitas": (
            "Asam lemah (pKa 4,76); bereaksi dengan basa membentuk garam asetat; "
            "esterifikasi dengan alkohol dengan katalis asam (reaksi reversibel); "
            "bereaksi dengan logam aktif (Zn, Fe) menghasilkan gas H₂; "
            "asam asetat glasial (>99%) bersifat korosif dan mudah terbakar (titik nyala 39°C); "
            "bereaksi dengan oksidator kuat meningkatkan risiko kebakaran; "
            "tidak kompatibel dengan kromat, permanganat, asam nitrat"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah dalam wadah plastik atau kaca berlabel "
            "'LIMBAH ASAM LEMAH – MUDAH TERBAKAR'.\n"
            "Langkah 2: Jauhkan dari sumber api (titik nyala 39°C untuk asam glasial).\n"
            "Langkah 3: Encerkan dengan air (1:5).\n"
            "Langkah 4: Netralisasi dengan NaHCO₃ atau NaOH encer hingga pH 6–8.\n"
            "Langkah 5: Buang ke saluran pembuangan dengan air mengalir. "
            "Konsentrasi glasial: serahkan ke pengelola limbah B3."
        ),
    },

    # ── BASA ────────────────────────────────────────────────────────
    "Natrium Hidroksida": {
        "rumus": "NaOH",
        "simbol_bahaya": "Korosif",
        # GHS: GHS05 (korosif)
        "wujud": "Padatan putih (pelet, serpih, atau granul)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Basa kuat; sangat reaktif dengan asam (netralisasi sangat eksotermis); "
            "bereaksi dengan logam amfoter Al dan Zn menghasilkan gas H₂ yang eksplosif; "
            "menyerap CO₂ dari udara membentuk Na₂CO₃ (higroskopis kuat); "
            "bereaksi eksotermis saat dilarutkan dalam air; "
            "tidak kompatibel dengan asam kuat, logam Al/Zn, halogen, asam nitrat"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah dalam wadah plastik HDPE berlabel "
            "'LIMBAH B3 – BASA KUAT'.\n"
            "Langkah 2: Netralisasi perlahan dengan HCl 10% atau H₂SO₄ encer sambil diaduk "
            "hingga pH 6–8.\n"
            "Langkah 3: Verifikasi pH dengan kertas indikator universal.\n"
            "Langkah 4: Encerkan dengan air mengalir (≥1:10).\n"
            "Langkah 5: Buang ke saluran pembuangan atau serahkan ke pengelola limbah B3."
        ),
    },
    "Kalium Hidroksida": {
        "rumus": "KOH",
        "simbol_bahaya": "Korosif",
        # GHS: GHS05 (korosif)
        "wujud": "Padatan putih (pelet atau lempeng)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Basa kuat lebih higroskopis dari NaOH; "
            "bereaksi sangat eksotermis dengan asam; "
            "bereaksi dengan logam Al dan Zn menghasilkan gas H₂; "
            "menyerap CO₂ dan uap air dari udara; "
            "sangat korosif terhadap jaringan hidup; "
            "tidak kompatibel dengan asam kuat, logam reaktif, halogen"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah dalam wadah plastik HDPE berlabel "
            "'LIMBAH B3 – BASA KUAT'.\n"
            "Langkah 2: Netralisasi perlahan dengan HCl 10% atau H₂SO₄ encer sambil diaduk "
            "hingga pH 6–8.\n"
            "Langkah 3: Verifikasi pH dengan kertas indikator universal.\n"
            "Langkah 4: Encerkan dengan air mengalir (≥1:10).\n"
            "Langkah 5: Buang ke saluran pembuangan atau serahkan ke pengelola limbah B3."
        ),
    },
    "Amonia": {
        "rumus": "NH₃",
        "simbol_bahaya": "Mudah Terbakar | Beracun | Korosif",
        # GHS: GHS02 (mudah terbakar), GHS06 (toksik akut), GHS05 (korosif)
        "wujud": "Gas tidak berwarna (atau cairan bertekanan); larutan berair (amonia encer)",
        "bau": "Sangat menyengat, khas amonia",
        "reaktivitas": (
            "Gas mudah terbakar dalam udara (batas ledakan 15–28%); "
            "bereaksi dengan asam membentuk garam amonium (eksotermis); "
            "bersifat basa lemah dalam air membentuk NH₄OH (pKb 4,74); "
            "bereaksi dengan ion logam transisi membentuk kompleks amina; "
            "bereaksi dengan oksidator (Cl₂, Br₂) menghasilkan nitrogen klorida yang eksplosif; "
            "toksik: LC₅₀ tikus 2.000 ppm (1 jam inhalasi); "
            "korosif terhadap Cu, Zn, dan paduan tembaga"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kerjakan di lemari asam berventilasi baik; gunakan APD lengkap.\n"
            "Langkah 2: Kumpulkan limbah larutan amonia dalam wadah plastik HDPE tertutup "
            "rapat, berlabel 'LIMBAH BASA – AMONIA'.\n"
            "Langkah 3: Encerkan dengan air (1:5) di area berventilasi.\n"
            "Langkah 4: Netralisasi dengan HCl encer hingga pH 6–8.\n"
            "Langkah 5: Buang ke saluran pembuangan dengan air mengalir. "
            "Gas amonia: alirkan ke larutan H₂SO₄ encer sebagai scrubber."
        ),
    },
    "Kalsium Hidroksida": {
        "rumus": "Ca(OH)₂",
        "simbol_bahaya": "Iritasi | Korosif",
        # GHS: GHS07 (iritasi), GHS05 (korosif pada mata/kulit basah)
        "wujud": "Serbuk putih halus",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Basa lemah hingga sedang (pH larutan jenuh ~12,4); "
            "bereaksi dengan asam membentuk garam kalsium (eksotermis); "
            "menyerap CO₂ dari udara membentuk CaCO₃ (lama-kelamaan mengeras); "
            "bereaksi lambat dengan air membentuk suspensi basa (slaked lime); "
            "tidak kompatibel dengan asam kuat, garam ammonium, fluorida"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan serbuk/suspensi dalam wadah plastik berlabel "
            "'LIMBAH BASA LEMAH'.\n"
            "Langkah 2: Encerkan dengan air (1:5) sambil diaduk.\n"
            "Langkah 3: Netralisasi dengan HCl encer hingga pH 6–8.\n"
            "Langkah 4: Buang ke saluran pembuangan dengan air mengalir. "
            "Endapan padatan buang ke tempat sampah non-organik."
        ),
    },

    # ── PELARUT ALKOHOL ───────────────────────────────────────────────
    "Etanol": {
        "rumus": "C₂H₅OH",
        "simbol_bahaya": "Mudah Terbakar",
        # GHS: GHS02 (mudah terbakar); etanol teknis dapat mengandung denaturant
        "wujud": "Cairan tidak berwarna",
        "bau": "Khas alkohol, agak manis",
        "reaktivitas": (
            "Cairan mudah terbakar (titik nyala 13°C); "
            "terbakar dengan nyala biru muda hampir tidak terlihat; "
            "bereaksi dengan oksidator kuat (KMnO₄, K₂Cr₂O₇) menghasilkan asetaldehida/asam asetat; "
            "bereaksi dengan Na dan K logam menghasilkan gas H₂; "
            "esterifikasi dengan asam karboksilat; "
            "stabil pada suhu kamar dalam wadah tertutup"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca atau logam berlabel "
            "'LIMBAH B3 – MUDAH TERBAKAR'.\n"
            "Langkah 2: Jangan campur dengan oksidator atau asam kuat.\n"
            "Langkah 3: Simpan di lemari asam berventilasi, jauh dari api dan sumber panas.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 untuk insinerasi suhu tinggi. "
            "Larutan encer (<24%) dengan kontaminan minimal dapat diencerkan ke >10:1 dan "
            "dibuang ke saluran dengan izin instansi setempat."
        ),
    },
    "Metanol": {
        "rumus": "CH₃OH",
        "simbol_bahaya": "Mudah Terbakar | Beracun",
        # GHS: GHS02 (mudah terbakar), GHS06 (toksik akut, Cat.3)
        "wujud": "Cairan tidak berwarna",
        "bau": "Khas alkohol (mirip etanol tetapi lebih lemah)",
        "reaktivitas": (
            "Cairan mudah terbakar (titik nyala 11°C); "
            "sangat toksik: dosis letal oral LD₅₀ manusia ~1 g/kg; termetabolisme menjadi "
            "formaldehida dan asam format yang menyerang saraf optik (kebutaan permanen); "
            "bereaksi dengan oksidator kuat menghasilkan formaldehida; "
            "bereaksi dengan Na/K logam menghasilkan gas H₂; "
            "tidak kompatibel dengan oksidator kuat, asam perklorat, asam kromat"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca atau logam tertutup rapat, "
            "berlabel 'LIMBAH B3 – MUDAH TERBAKAR BERACUN'.\n"
            "Langkah 2: Jangan campur dengan oksidator atau asam kuat.\n"
            "Langkah 3: Simpan di lemari asam berventilasi, jauh dari api dan panas.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 untuk insinerasi suhu tinggi. "
            "JANGAN buang ke saluran umum — toksik bagi organisme akuatik."
        ),
    },
    "Isopropanol": {
        "rumus": "C₃H₇OH (2-propanol)",
        "simbol_bahaya": "Mudah Terbakar | Iritasi",
        # GHS: GHS02 (mudah terbakar), GHS07 (iritasi)
        "wujud": "Cairan tidak berwarna",
        "bau": "Khas alkohol, lebih menyengat dari etanol",
        "reaktivitas": (
            "Cairan mudah terbakar (titik nyala 12°C); "
            "terbakar dengan nyala terang biru; "
            "teroksidasi oleh oksidator kuat menjadi aseton; "
            "bereaksi dengan Na/K logam menghasilkan gas H₂; "
            "tidak kompatibel dengan oksidator, asam kuat, basa kuat; "
            "stabil pada suhu kamar dalam wadah tertutup"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca atau logam berlabel "
            "'LIMBAH B3 – MUDAH TERBAKAR'.\n"
            "Langkah 2: Jangan campur dengan oksidator atau asam kuat.\n"
            "Langkah 3: Simpan di lemari asam berventilasi, jauh dari api dan panas.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 untuk insinerasi suhu tinggi."
        ),
    },

    # ── PELARUT KETON & ESTER ─────────────────────────────────────────
    "Aseton": {
        "rumus": "(CH₃)₂CO",
        "simbol_bahaya": "Mudah Terbakar | Iritasi",
        # GHS: GHS02 (mudah terbakar), GHS07 (iritasi)
        "wujud": "Cairan tidak berwarna",
        "bau": "Khas manis-aromatik",
        "reaktivitas": (
            "Cairan sangat mudah terbakar (titik nyala −18°C, batas ledakan 2,5–12,8%); "
            "bereaksi dengan oksidator kuat (H₂O₂, HNO₃) secara eksotermis; "
            "membentuk aseton peroksida eksplosif dengan H₂O₂ pekat; "
            "bereaksi dengan kloroform + NaOH menghasilkan kloropikrin toksik; "
            "melarutkan banyak polimer dan plastik; stabil dalam kondisi normal"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca atau logam tertutup rapat, "
            "berlabel 'LIMBAH B3 – MUDAH TERBAKAR'.\n"
            "Langkah 2: Jangan campur dengan oksidator, asam kuat, atau basa kuat.\n"
            "Langkah 3: Simpan di lemari asam berventilasi, jauh dari api dan percikan listrik.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 untuk insinerasi atau daur ulang pelarut."
        ),
    },
    "Etil Asetat": {
        "rumus": "CH₃COOC₂H₅",
        "simbol_bahaya": "Mudah Terbakar | Iritasi",
        # GHS: GHS02 (mudah terbakar), GHS07 (iritasi)
        "wujud": "Cairan tidak berwarna",
        "bau": "Bau buah-fruity, manis",
        "reaktivitas": (
            "Cairan mudah terbakar (titik nyala −4°C); "
            "terhidrolisis dalam suasana basa kuat menjadi asam asetat dan etanol (saponifikasi); "
            "bereaksi dengan asam dan basa kuat; "
            "bereaksi dengan oksidator; "
            "stabil dalam kondisi netral dan suhu kamar"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca atau logam berlabel "
            "'LIMBAH B3 – MUDAH TERBAKAR'.\n"
            "Langkah 2: Jangan campur dengan oksidator atau asam/basa kuat.\n"
            "Langkah 3: Simpan di lemari asam berventilasi, jauh dari api dan panas.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 untuk insinerasi atau daur ulang pelarut."
        ),
    },

    # ── PELARUT HIDROKARBON ───────────────────────────────────────────
    "n-Heksana": {
        "rumus": "C₆H₁₄",
        "simbol_bahaya": "Sangat Mudah Terbakar | Beracun | Bahaya Lingkungan",
        # GHS: GHS02 (mudah terbakar), GHS07 (iritasi/toksik), GHS08 (toksik kronis/reproduksi),
        #       GHS09 (bahaya lingkungan)
        "wujud": "Cairan tidak berwarna",
        "bau": "Seperti bensin/petrol",
        "reaktivitas": (
            "Sangat mudah terbakar (titik nyala −22°C, batas ledakan 1,1–7,5%); "
            "stabil pada suhu kamar; inert terhadap asam dan basa encer; "
            "uap lebih berat dari udara — dapat terakumulasi di cekungan rendah; "
            "neurotoksik kronik: metabolit 2,5-heksandion merusak saraf perifer; "
            "bahaya lingkungan: toksik bagi organisme akuatik"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah logam atau kaca tertutup rapat berlabel "
            "'LIMBAH B3 – MUDAH TERBAKAR BERACUN'.\n"
            "Langkah 2: Simpan di lemari asam berventilasi, jauh dari api dan oksidator.\n"
            "Langkah 3: JANGAN buang ke saluran pembuangan (toksik lingkungan).\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk insinerasi "
            "atau daur ulang pelarut."
        ),
    },
    "Dietil Eter": {
        "rumus": "(C₂H₅)₂O",
        "simbol_bahaya": "Sangat Mudah Terbakar | Eksplosif",
        # GHS: GHS02 (sangat mudah terbakar), GHS07 (iritasi)
        # PERHATIAN KHUSUS: pembentukan peroksida!
        "wujud": "Cairan tidak berwarna",
        "bau": "Manis khas eter",
        "reaktivitas": (
            "Sangat mudah terbakar (titik nyala −45°C, batas ledakan 1,9–36%); "
            "BAHAYA PEROKSIDA: membentuk peroksida eksplosif jika terpapar udara dan cahaya "
            "dalam waktu lama — uji peroksida sebelum distilasi; "
            "uap lebih berat dari udara — menyambar dari jarak jauh; "
            "dapat teranestesi pada konsentrasi tinggi; "
            "tidak kompatibel dengan oksidator kuat, halogen, asam kuat"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Uji kandungan peroksida dahulu menggunakan strip uji peroksida. "
            "Jika positif, JANGAN dipindahkan — hubungi ahli bahan berbahaya.\n"
            "Langkah 2: Kumpulkan dalam wadah logam atau kaca gelap berlabel "
            "'LIMBAH B3 – SANGAT MUDAH TERBAKAR'.\n"
            "Langkah 3: Simpan jauh dari cahaya, api, dan oksidator.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk insinerasi."
        ),
    },
    "Benzena": {
        "rumus": "C₆H₆",
        "simbol_bahaya": "Karsinogen | Mudah Terbakar | Beracun | Bahaya Lingkungan",
        # GHS: GHS02, GHS06, GHS08 (karsinogen Kel.1A), GHS09
        "wujud": "Cairan tidak berwarna",
        "bau": "Aromatis khas",
        "reaktivitas": (
            "Mudah terbakar (titik nyala −11°C, batas ledakan 1,2–7,8%); "
            "bereaksi substitusi elektrofilik aromatik (nitrasi, sulfonasi, halogenasi, "
            "alkilasi Friedel-Crafts); "
            "karsinogen Kelompok 1A IARC: menyebabkan leukemia (AML); "
            "toksik bagi sumsum tulang; "
            "terbakar dengan nyala berjelaga hitam"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca atau logam tertutup rapat berlabel "
            "'LIMBAH B3 – KARSINOGEN MUDAH TERBAKAR'.\n"
            "Langkah 2: Simpan di lemari asam berventilasi, jauh dari api dan oksidator.\n"
            "Langkah 3: JANGAN buang ke saluran pembuangan — karsinogen dan racun lingkungan.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk insinerasi suhu tinggi. "
            "Gunakan APD lengkap termasuk respirator saat penanganan."
        ),
    },
    "Toluena": {
        "rumus": "C₇H₈",
        "simbol_bahaya": "Mudah Terbakar | Beracun | Bahaya Reproduksi",
        # GHS: GHS02 (mudah terbakar), GHS07 (iritasi), GHS08 (reproduksi Cat.2)
        "wujud": "Cairan tidak berwarna",
        "bau": "Aromatis khas (mirip benzena tetapi tidak sekuat itu)",
        "reaktivitas": (
            "Mudah terbakar (titik nyala 4°C, batas ledakan 1,1–7,1%); "
            "bereaksi substitusi elektrofilik aromatik lebih reaktif dari benzena (gugus CH₃ orto/para-director); "
            "teroksidasi oleh KMnO₄ menghasilkan asam benzoat; "
            "toksik SSP (narcosis); bahaya reproduksi Cat.2 GHS; "
            "terbakar dengan nyala berjelaga; "
            "tidak kompatibel dengan oksidator kuat, asam nitrat pekat"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca atau logam berlabel "
            "'LIMBAH B3 – MUDAH TERBAKAR BERACUN'.\n"
            "Langkah 2: Simpan di lemari asam berventilasi, jauh dari api dan oksidator.\n"
            "Langkah 3: JANGAN buang ke saluran pembuangan.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk insinerasi "
            "atau daur ulang pelarut."
        ),
    },

    # ── PELARUT TERKLORINASI ──────────────────────────────────────────
    "Kloroform": {
        "rumus": "CHCl₃",
        "simbol_bahaya": "Beracun | Karsinogen | Iritasi",
        # GHS: GHS06 (toksik akut), GHS08 (karsinogen Cat.2, hepatotoksik)
        "wujud": "Cairan tidak berwarna, berat",
        "bau": "Manis khas (seperti eter)",
        "reaktivitas": (
            "Tidak mudah terbakar; "
            "terurai oleh cahaya UV dan udara perlahan membentuk fosgen (COCl₂) — "
            "sangat toksik; disimpan dengan stabilizer etanol (0,5–1%) untuk mencegah oksidasi; "
            "bereaksi dengan basa kuat menghasilkan karbena; "
            "hepatotoksik dan nefrotoksik; karsinogen Cat.2 GHS; "
            "toksik akut melalui inhalasi dan ingesti"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca gelap berlabel "
            "'LIMBAH B3 – TOKSIK HALOGEN'. JANGAN campur dengan limbah lain.\n"
            "Langkah 2: Simpan dingin, hindari cahaya langsung.\n"
            "Langkah 3: Hindari kontak kulit/inhalasi — gunakan APD lengkap.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk pengolahan khusus "
            "(insinerasi suhu tinggi dengan scrubber HCl)."
        ),
    },
    "Diklorometana": {
        "rumus": "CH₂Cl₂",
        "simbol_bahaya": "Beracun | Iritasi | Karsinogen (Mungkin)",
        # GHS: GHS07 (iritasi), GHS08 (karsinogen Cat.2)
        # KOREKSI: bukan "mudah terbakar" — DCM tidak mudah terbakar!
        "wujud": "Cairan tidak berwarna",
        "bau": "Manis khas (seperti kloroform)",
        "reaktivitas": (
            "TIDAK mudah terbakar (titik nyala tidak ada dalam kondisi normal); "
            "stabil pada suhu kamar; terurai pada suhu tinggi (>120°C) menghasilkan HCl dan COCl₂; "
            "bereaksi lambat dengan basa kuat; "
            "pelarut organik inert yang relatif aman secara kimiawi; "
            "toksik melalui inhalasi (konversi hepatik menjadi CO); "
            "karsinogen kategori 2 (IARC Kelompok 2A)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca atau HDPE berlabel "
            "'LIMBAH B3 – TOKSIK HALOGEN'. JANGAN campur dengan limbah lain.\n"
            "Langkah 2: Simpan dalam wadah tertutup rapat di tempat dingin dan berventilasi.\n"
            "Langkah 3: Hindari inhalasi uap — gunakan APD.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk insinerasi "
            "dengan scrubber."
        ),
    },
    "Karbon Tetraklorida": {
        "rumus": "CCl₄",
        "simbol_bahaya": "Beracun | Karsinogen | Bahaya Lingkungan | Perusak Ozon",
        # GHS: GHS06 (toksik akut), GHS08 (karsinogen Cat.2, hepatotoksik), GHS09 (lingkungan)
        "wujud": "Cairan tidak berwarna, berat (ρ = 1,59 g/mL)",
        "bau": "Manis khas, tidak menyengat",
        "reaktivitas": (
            "TIDAK mudah terbakar; "
            "sangat stabil secara kimia; terurai pada suhu tinggi menghasilkan fosgen (COCl₂) dan HCl; "
            "inert terhadap asam, basa, dan oksidator encer; "
            "merusak lapisan ozon stratosfer (ODS — diatur Montreal Protocol); "
            "hepatotoksik dan nefrotoksik kuat; "
            "karsinogen hati (IARC Kelompok 2B)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca gelap berlabel "
            "'LIMBAH B3 – TOKSIK HALOGEN – PERUSAK OZON'.\n"
            "Langkah 2: JANGAN campur dengan limbah lain atau bahan mudah terbakar.\n"
            "Langkah 3: Simpan di tempat dingin, berventilasi, jauh dari panas.\n"
            "Langkah 4: Serahkan SEGERA ke pengelola limbah B3 bersertifikat — "
            "dilarang dilepas ke atmosfer (regulasi ODS)."
        ),
    },

    # ── OKSIDATOR ─────────────────────────────────────────────────────
    "Hidrogen Peroksida": {
        "rumus": "H₂O₂",
        "simbol_bahaya": "Oksidator | Korosif",
        # GHS: GHS03 (oksidator), GHS05 (korosif) untuk konsentrasi >30%
        "wujud": "Cairan tidak berwarna",
        "bau": "Bau tajam seperti ozon (konsentrasi tinggi)",
        "reaktivitas": (
            "Oksidator kuat (semakin pekat semakin reaktif); "
            "terurai terkena cahaya, panas, logam (MnO₂, Fe, Cu), atau kontaminan organik "
            "menghasilkan O₂ dan H₂O (terurai akselerasi pada >70°C); "
            "bereaksi hebat dengan bahan organik, alcohol, dan agen pereduksi; "
            "H₂O₂ >30% bersifat korosif; >70% dapat memicu kebakaran spontan "
            "dengan bahan organik; tidak boleh disimpan dalam wadah tertutup rapat "
            "(risiko tekanan O₂)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik HDPE berlabel "
            "'LIMBAH B3 – OKSIDATOR'. JANGAN campur dengan bahan organik.\n"
            "Langkah 2: Encerkan perlahan dengan air dingin (1:10).\n"
            "Langkah 3: Jika konsentrasi pekat (>30%), netralkan dengan Na₂SO₃ encer terlebih dahulu.\n"
            "Langkah 4: Verifikasi pH 6–8.\n"
            "Langkah 5: Untuk konsentrasi <3%: dapat dibuang ke saluran dengan air mengalir. "
            "Konsentrasi tinggi: serahkan ke pengelola limbah B3."
        ),
    },
    "Kalium Permanganat": {
        "rumus": "KMnO₄",
        "simbol_bahaya": "Oksidator | Beracun | Iritasi | Bahaya Lingkungan",
        # GHS: GHS03, GHS06, GHS07, GHS09
        "wujud": "Padatan kristal ungu tua",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Oksidator sangat kuat, terutama dalam suasana asam; "
            "bereaksi hebat dan meledak dengan asam sulfat pekat, alkohol, gliserin, "
            "bahan organik, dan agen pereduksi; "
            "larutan ungu berubah coklat/hitam (MnO₂) saat tereduksi; "
            "dapat menyulut kebakaran spontan jika kontak dengan bahan organik; "
            "tidak kompatibel dengan H₂SO₄ pekat, gliserin, etanol, NH₄⁺"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik atau kaca berlabel "
            "'LIMBAH B3 – OKSIDATOR'. JANGAN campur dengan bahan organik/pereduksi.\n"
            "Langkah 2: Encerkan dengan air (1:10) secara perlahan.\n"
            "Langkah 3: Reduksi dengan natrium tiosulfat (Na₂S₂O₃) atau asam oksalat "
            "hingga larutan tidak berwarna.\n"
            "Langkah 4: Netralisasi pH hingga 6–8.\n"
            "Langkah 5: Serahkan ke pengelola limbah B3 — Mn adalah logam berat."
        ),
    },
    "Kalium Dikromat": {
        "rumus": "K₂Cr₂O₇",
        "simbol_bahaya": "Oksidator | Toksik | Karsinogen | Korosif | Bahaya Lingkungan",
        # GHS: GHS03, GHS06, GHS08 (karsinogen Kel.1A), GHS05, GHS09
        "wujud": "Padatan kristal jingga-merah",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Oksidator kuat dalam suasana asam (Cr VI sangat reaktif); "
            "bereaksi dengan alkohol dan senyawa organik lainnya; "
            "larutan jingga berubah hijau (Cr³⁺) saat tereduksi; "
            "karsinogen Kelompok 1A IARC (penyebab kanker paru); "
            "toksik dan sensitizer kulit; "
            "tidak kompatibel dengan pereduksi kuat, bahan organik, asam hidroklorida"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik berlabel "
            "'LIMBAH B3 – OKSIDATOR TOKSIK KARSINOGEN'. JANGAN campur dengan bahan organik.\n"
            "Langkah 2: Encerkan dengan air (1:10) secara perlahan.\n"
            "Langkah 3: Reduksi Cr(VI) menjadi Cr(III) dengan Na₂S₂O₃ atau FeSO₄ dalam suasana asam.\n"
            "Langkah 4: Netralisasi dengan NaOH untuk mengendapkan Cr(OH)₃.\n"
            "Langkah 5: Saring endapan; serahkan ke pengelola limbah B3 bersertifikat "
            "— Cr(VI) adalah limbah B3 karsinogen."
        ),
    },

    # ── SENYAWA EKSPLOSIF/REAKTIF SANGAT BAHAYA ──────────────────────
    "Natrium Azida": {
        "rumus": "NaN₃",
        "simbol_bahaya": "Beracun | Eksplosif | Bahaya Lingkungan",
        # GHS: GHS06 (toksik akut), GHS01 (eksplosif), GHS09 (lingkungan)
        "wujud": "Padatan kristalin putih",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Eksplosif jika dipanaskan, terkena gesekan, atau benturan; "
            "bereaksi dengan asam menghasilkan asam hidrazida (HN₃) — sangat beracun dan eksplosif; "
            "bereaksi dengan logam Cu, Pb, Ag, dan Cu membentuk azida logam yang sangat sensitif-peka; "
            "toksik akut sangat tinggi (LD₅₀ tikus oral = 27 mg/kg); "
            "menghambat sitokrom c oksidase (mirip sianida); "
            "JANGAN masukkan ke sistem pipa tembaga/timbal"
        ),
        "pengelolaan_limbah": (
            "⚠️ PERHATIAN EKSPLOSIF DAN SANGAT BERACUN!\n"
            "Langkah 1: JANGAN terpapar panas, gesekan, atau benturan.\n"
            "Langkah 2: Simpan dalam wadah asli, jangan dipindahkan jika tidak perlu.\n"
            "Langkah 3: Untuk dekontaminasi kecil: larutkan perlahan dalam larutan NaNO₂ asam "
            "(reaksi dekomposisi aman) — HANYA oleh personel terlatih.\n"
            "Langkah 4: Beri label 'LIMBAH EKSPLOSIF BERACUN – NaN₃'.\n"
            "Langkah 5: Serahkan ke pengelola limbah B3 khusus bahan eksplosif."
        ),
    },
    "Asam Pikrat": {
        "rumus": "C₆H₃N₃O₇ (2,4,6-trinitrofenol)",
        "simbol_bahaya": "Eksplosif | Beracun",
        # GHS: GHS01 (eksplosif), GHS06 (toksik)
        "wujud": "Padatan kristal kuning",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Eksplosif kuat jika kering, dipanaskan, digesekan, atau dibanting; "
            "lebih sensitif dari TNT dalam keadaan kering; "
            "bereaksi dengan basa membentuk pikrat logam yang lebih peka/eksplosif "
            "(pikrat Pb, pikrat Fe sangat berbahaya); "
            "oksidator kuat; toksik melalui ingesti dan inhalasi; "
            "HARUS SELALU DIJAGA BASAH (>10% air) untuk keamanan"
        ),
        "pengelolaan_limbah": (
            "⚠️ PERHATIAN EKSPLOSIF: JANGAN DIKERINGKAN ATAU DIGETARKAN!\n"
            "Langkah 1: JAGA tetap basah dengan air (minimal 10–30% kadar air).\n"
            "Langkah 2: Kumpulkan dalam wadah plastik khusus berlabel "
            "'LIMBAH EKSPLOSIF – ASAM PIKRAT – JAGA BASAH'.\n"
            "Langkah 3: Hindari gesekan, panas, dan benturan selama penanganan.\n"
            "Langkah 4: Serahkan SEGERA ke pengelola limbah B3 khusus bahan eksplosif. "
            "JANGAN disimpan dalam jangka panjang."
        ),
    },
    "Benzoil Peroksida": {
        "rumus": "C₁₄H₁₀O₄",
        "simbol_bahaya": "Eksplosif | Oksidator | Iritasi",
        # GHS: GHS01 (eksplosif), GHS03 (oksidator), GHS07 (iritasi)
        "wujud": "Padatan putih granular (biasanya dibasahi ≥30% air)",
        "bau": "Tidak berbau (lemah)",
        "reaktivitas": (
            "Eksplosif jika dipanaskan (>80°C) atau terkena gesekan/benturan dalam keadaan kering; "
            "terurai menjadi radikal benzoiloksi bebas; "
            "inisiator polimerisasi radikal bebas; "
            "bereaksi hebat dengan agen pereduksi, asam, dan basa; "
            "oksidator kuat; sensitif terhadap kontaminasi logam; "
            "stabilitas termal rendah; titik leleh juga titik dekomposisi"
        ),
        "pengelolaan_limbah": (
            "⚠️ PERHATIAN EKSPLOSIF!\n"
            "Langkah 1: JANGAN terpapar panas >80°C, gesekan, atau benturan.\n"
            "Langkah 2: Simpan dalam wadah asli yang dibasahi, jangan dipindahkan jika tidak perlu.\n"
            "Langkah 3: Beri label 'LIMBAH EKSPLOSIF – BENZOIL PEROKSIDA'.\n"
            "Langkah 4: Serahkan SEGERA ke pengelola limbah B3 khusus bahan eksplosif."
        ),
    },

    # ── GARAM ANORGANIK UMUM ──────────────────────────────────────────
    "Natrium Klorida": {
        "rumus": "NaCl",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak memiliki piktogram bahaya
        "wujud": "Padatan kristal putih (kubik)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Sangat stabil; tidak reaktif terhadap air, udara, atau asam encer; "
            "terdisosiasi sempurna dalam air menjadi ion Na⁺ dan Cl⁻; "
            "titik leleh tinggi (801°C); "
            "bereaksi dengan H₂SO₄ pekat menghasilkan gas HCl; "
            "tidak mudah terbakar"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir.\n"
            "Langkah 3: Padatan bersih dapat dibuang ke tempat sampah umum."
        ),
    },
    "Kalium Klorida": {
        "rumus": "KCl",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram bahaya
        "wujud": "Padatan kristal putih atau tidak berwarna",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Sangat stabil; tidak reaktif terhadap air, udara, atau asam encer; "
            "terdisosiasi sempurna dalam air menjadi ion K⁺ dan Cl⁻; "
            "titik leleh tinggi (770°C); tidak mudah terbakar; "
            "LD₅₀ oral tikus 2.500 mg/kg (toksisitas sangat rendah)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir.\n"
            "Langkah 3: Padatan bersih dapat dibuang ke tempat sampah umum."
        ),
    },
    "Kalsium Klorida": {
        "rumus": "CaCl₂",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi kulit/mata)
        "wujud": "Padatan putih granul, pelet, atau serpih (higroskopis kuat)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Higroskopis kuat (menyerap uap air dari udara); "
            "bereaksi eksotermis dengan air saat dilarutkan; "
            "stabil pada suhu kamar dalam wadah tertutup; "
            "tidak reaktif terhadap logam dalam kondisi normal; "
            "bereaksi dengan florida, sulfat membentuk endapan"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Netralisasi pH jika perlu hingga 6–8.\n"
            "Langkah 3: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Magnesium Sulfat": {
        "rumus": "MgSO₄",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram bahaya
        "wujud": "Padatan putih (anhidrat) atau kristal putih (heptahidrat/garam Epsom)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; larut dalam air (eksotermis ringan); "
            "tidak reaktif terhadap asam dan basa encer; "
            "anhidrat bersifat desikan (higroskopis); "
            "terurai pada suhu tinggi (>1.124°C)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Natrium Sulfat": {
        "rumus": "Na₂SO₄",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram
        "wujud": "Padatan putih (anhidrat) atau kristal tidak berwarna (dekahidrat, garam Glauber)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Sangat stabil; tidak reaktif terhadap air, udara, atau asam/basa encer; "
            "larut dalam air tanpa reaksi signifikan; tidak mudah terbakar"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Natrium Karbonat": {
        "rumus": "Na₂CO₃",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi kulit/mata)
        "wujud": "Serbuk putih (anhidrat) atau granul",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Basa lemah (pH larutan 1% ≈ 11,6); "
            "bereaksi dengan asam menghasilkan CO₂ dan air (effervescence nyata); "
            "bereaksi dengan ion logam berat membentuk endapan karbonat; "
            "hidrolisis lambat dalam air menghasilkan OH⁻; "
            "tidak mudah terbakar"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah dalam wadah berlabel 'LIMBAH BASA LEMAH'.\n"
            "Langkah 2: Encerkan dengan air (1:5).\n"
            "Langkah 3: Netralisasi dengan HCl encer hingga pH 6–8.\n"
            "Langkah 4: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Natrium Bikarbonat": {
        "rumus": "NaHCO₃",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram bahaya
        "wujud": "Serbuk putih halus",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil dalam bentuk padat; "
            "terurai pada suhu >50°C (mulai dekomposisi) → Na₂CO₃ + H₂O + CO₂; "
            "terurai sempurna ~270°C; "
            "bereaksi dengan asam menghasilkan CO₂ (effervescence kuat); "
            "buffer pH lemah; tidak mudah terbakar"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir. "
            "Tidak diperlukan penanganan khusus B3."
        ),
    },

    # ── GARAM LOGAM BERAT / TOKSIK ────────────────────────────────────
    "Tembaga(II) Sulfat": {
        "rumus": "CuSO₄",
        "simbol_bahaya": "Beracun | Iritasi | Bahaya Lingkungan",
        # GHS: GHS06 (toksik), GHS07 (iritasi), GHS09 (bahaya lingkungan)
        "wujud": "Padatan kristal biru (pentahidrat); putih (anhidrat)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "bentuk anhidrat (putih) sangat higroskopis → biru saat menyerap air; "
            "bereaksi dengan basa membentuk endapan Cu(OH)₂ biru pucat; "
            "toksik bagi organisme akuatik dan manusia (LD₅₀ tikus oral 300 mg/kg); "
            "bioakumulatif di ekosistem akuatik; "
            "fungisida pertanian; bereaksi dengan Fe dan Zn (pergeseran logam)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik HDPE berlabel 'LIMBAH LOGAM BERAT – Cu'.\n"
            "Langkah 2: JANGAN campur dengan limbah organik atau asam kuat.\n"
            "Langkah 3: Endapkan logam dengan NaOH → Cu(OH)₂; saring dan keringkan.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk daur ulang logam.\n"
            "Langkah 5: JANGAN buang ke lingkungan — bioakumulatif."
        ),
    },
    "Besi(III) Klorida": {
        "rumus": "FeCl₃",
        "simbol_bahaya": "Korosif | Iritasi",
        # GHS: GHS05 (korosif), GHS07 (iritasi)
        # KOREKSI: "Beracun" dihapus — FeCl₃ bukan toksik sistemik tinggi, tapi korosif
        "wujud": "Padatan coklat-hitam (anhidrat) atau kuning-coklat (heksahidrat)",
        "bau": "Bau asam lemah (hidrolisis menghasilkan HCl)",
        "reaktivitas": (
            "Higroskopis kuat; "
            "terhidrolisis dalam air membentuk larutan asam (Fe³⁺ + 3H₂O → Fe(OH)₃ + 3H⁺); "
            "oksidator lemah sampai sedang; "
            "korosif terhadap banyak logam; "
            "bereaksi dengan basa membentuk endapan Fe(OH)₃ coklat; "
            "tidak kompatibel dengan basa kuat, logam alkali, agen pereduksi"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik berlabel 'LIMBAH B3 – KOROSIF'.\n"
            "Langkah 2: Encerkan dengan air (1:5).\n"
            "Langkah 3: Netralisasi dengan NaOH encer hingga pH 6–8 → terbentuk endapan Fe(OH)₃.\n"
            "Langkah 4: Saring endapan, keringkan, buang ke limbah B3 padat.\n"
            "Langkah 5: Filtrat cair dapat dibuang ke saluran pembuangan."
        ),
    },
    "Barium Klorida": {
        "rumus": "BaCl₂",
        "simbol_bahaya": "Beracun | Iritasi",
        # GHS: GHS06 (toksik akut), GHS07 (iritasi)
        "wujud": "Padatan kristal putih",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; larut dalam air; "
            "bereaksi dengan sulfat membentuk endapan BaSO₄ putih tidak larut (uji kualitatif sulfat); "
            "toksik: LD₅₀ tikus oral = 118–250 mg/kg (toksik akut tinggi); "
            "menyebabkan hipokalemia (menurunkan K⁺ darah); "
            "tidak kompatibel dengan asam kuat, sulfat, permanganat"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik berlabel 'LIMBAH LOGAM BERAT – Ba'.\n"
            "Langkah 2: JANGAN campur dengan limbah organik atau asam sulfat "
            "(pengendapan BaSO₄ mungkin bermanfaat tapi pastikan Ba terambil).\n"
            "Langkah 3: Endapkan Ba²⁺ dengan Na₂SO₄ → BaSO₄ tidak larut.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 untuk pengolahan khusus."
        ),
    },
    "Stronsium Klorida": {
        "rumus": "SrCl₂",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi)
        "wujud": "Padatan kristal putih (atau heksahidrat)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; larut dalam air; "
            "memberikan nyala merah karmin pada uji nyala api (emisi Sr pada 640 dan 671 nm); "
            "digunakan dalam piroteknik; "
            "tidak reaktif terhadap asam/basa encer; "
            "toksisitas rendah-sedang (mirip CaCl₂)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Netralisasi pH jika perlu hingga 6–8.\n"
            "Langkah 3: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Amonium Klorida": {
        "rumus": "NH₄Cl",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi)
        "wujud": "Padatan kristal putih",
        "bau": "Tidak berbau (sedikit berbau amonia jika basah)",
        "reaktivitas": (
            "Stabil pada suhu kamar dalam wadah tertutup; "
            "terurai reversibel pada ~338°C → NH₃ + HCl; "
            "bereaksi dengan basa kuat menghasilkan gas amonia; "
            "larut dalam air (endotermis, menurunkan suhu); "
            "asam lemah dalam larutan; "
            "tidak mudah terbakar"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Netralisasi pH jika perlu hingga 6–8.\n"
            "Langkah 3: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },

    # ── INDIKATOR ASAM-BASA ───────────────────────────────────────────
    "Fenolftalein": {
        "rumus": "C₂₀H₁₄O₄",
        "simbol_bahaya": "Iritasi | Karsinogen (Mungkin)",
        # GHS: GHS07 (iritasi), GHS08 (karsinogen Cat.2)
        # KOREKSI: Fenolftalein IARC Kelompok 2B (mungkin karsinogen pada manusia)
        "wujud": "Padatan kristal putih hingga kuning muda",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "indikator asam-basa: tidak berwarna pada pH <8,2; merah muda/merah pada pH >8,3–10; "
            "tidak berwarna kembali pada pH >12 (bentuk trifenol); "
            "tidak reaktif dalam kondisi normal; "
            "toksisitas rendah-sedang; karsinogen Cat.2 GHS"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah larutan dalam wadah kaca berlabel "
            "'LIMBAH B3 – INDIKATOR'.\n"
            "Langkah 2: Encerkan dengan air (1:10).\n"
            "Langkah 3: Serahkan limbah pekat ke pengelola limbah B3."
        ),
    },
    "Metil Jingga": {
        "rumus": "C₁₄H₁₄N₃NaO₃S",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi)
        "wujud": "Serbuk jingga-kuning",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "indikator pH: merah pada pH <3,1; jingga pada pH 3,1–4,4; kuning pada pH >4,4; "
            "sensitif terhadap cahaya (fotodegradasi lambat); "
            "tidak reaktif dalam kondisi normal"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah larutan dalam wadah kaca berlabel "
            "'LIMBAH B3 – INDIKATOR'.\n"
            "Langkah 2: Encerkan dengan air (1:10).\n"
            "Langkah 3: Serahkan limbah pekat ke pengelola limbah B3."
        ),
    },
    "Bromtimol Biru": {
        "rumus": "C₂₇H₂₈Br₂O₅S",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi ringan)
        "wujud": "Serbuk kristal kuning-coklat",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "indikator pH: kuning pada pH <6,0; hijau pada pH 6,0–7,6; biru pada pH >7,6; "
            "tidak reaktif dalam kondisi normal; "
            "digunakan luas dalam biokimia dan analitik"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah larutan dalam wadah kaca berlabel "
            "'LIMBAH B3 – INDIKATOR'.\n"
            "Langkah 2: Encerkan dengan air (1:10).\n"
            "Langkah 3: Serahkan limbah pekat ke pengelola limbah B3."
        ),
    },
    "Metil Merah": {
        "rumus": "C₁₅H₁₅N₃O₂",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi)
        "wujud": "Padatan kristal merah-jingga gelap",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "indikator pH: merah pada pH <4,4; jingga pada pH 4,4–6,2; kuning pada pH >6,2; "
            "tidak reaktif dalam kondisi normal; "
            "digunakan dalam titrasi asam-basa (range lebih sempit dari metil jingga)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah larutan dalam wadah kaca berlabel "
            "'LIMBAH B3 – INDIKATOR'.\n"
            "Langkah 2: Encerkan dengan air (1:10).\n"
            "Langkah 3: Serahkan limbah pekat ke pengelola limbah B3."
        ),
    },

    # ── PEREAKSI ANALITIK & REAGEN ────────────────────────────────────
    "EDTA": {
        "rumus": "C₁₀H₁₆N₂O₈ (asam bebas) / Na₂EDTA (garam dinatrium)",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi) untuk garam
        "wujud": "Serbuk putih kristalin",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "agen pengkhelat sangat kuat untuk ion logam divalen dan trivalen "
            "(Ca²⁺, Mg²⁺, Fe³⁺, Cu²⁺, Zn²⁺); "
            "larut baik dalam basa (pKa₁=2,0; pKa₂=2,7; pKa₃=6,2; pKa₄=10,3); "
            "tidak mudah terbakar; relatif inert secara kimia"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Netralisasi pH jika perlu hingga 6–8.\n"
            "Langkah 3: Buang ke saluran pembuangan dengan air mengalir. "
            "Catatan: EDTA dapat memobilisasi logam berat di lingkungan — "
            "hindari jumlah besar ke perairan."
        ),
    },
    "Pereaksi Biuret": {
        "rumus": "Campuran: CuSO₄ + NaOH (atau NaKC₄H₄O₆)",
        # KOREKSI: rumus sebelumnya "Biuret reagent" tidak informatif
        "simbol_bahaya": "Korosif | Iritasi",
        # GHS: GHS05 (NaOH korosif), GHS07 (CuSO₄ iritasi)
        "wujud": "Larutan biru (mengandung CuSO₄ dalam NaOH)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Komponen NaOH bersifat korosif kuat; "
            "bereaksi dengan ikatan peptida (-CO-NH-) dalam suasana basa membentuk kompleks "
            "ungu (Cu²⁺-protein, reaksi Biuret); "
            "peka terhadap cahaya dan suhu tinggi; "
            "tidak kompatibel dengan asam kuat"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah cair dalam wadah plastik berlabel "
            "'LIMBAH B3 – REAGEN LOGAM'.\n"
            "Langkah 2: Netralisasi pH dengan HCl encer hingga 6–8.\n"
            "Langkah 3: Endapkan Cu²⁺ dengan NaOH jika konsentrasi tinggi.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3."
        ),
    },
    "Pereaksi Ninhidrin": {
        "rumus": "C₉H₆O₄ (2,2-dihidroksi-1H-inden-1,3(2H)-dion)",
        "simbol_bahaya": "Beracun | Iritasi",
        # GHS: GHS06 (toksik akut), GHS07 (iritasi)
        # KOREKSI: ninhidrin lebih tepat dikategorikan toksik, bukan hanya iritasi
        "wujud": "Padatan kristal kuning pucat (stabil); larutan dalam aseton/etanol",
        "bau": "Tidak berbau (padatan); bau pelarut jika dalam larutan",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "bereaksi spesifik dengan asam amino bebas (gugus -NH₂) membentuk kompleks "
            "ungu/biru (Ruhemann's purple, λmax = 570 nm); "
            "bereaksi dengan amina primer dan sekunder; "
            "sensitif terhadap cahaya (degradasi bertahap); "
            "dilarutkan dalam aseton atau etanol untuk digunakan"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah larutan dalam wadah kaca berlabel "
            "'LIMBAH B3 – REAGEN ANALITIK'.\n"
            "Langkah 2: Encerkan dengan air (1:10).\n"
            "Langkah 3: Serahkan limbah pekat ke pengelola limbah B3."
        ),
    },
    "Perak Nitrat": {
        "rumus": "AgNO₃",
        "simbol_bahaya": "Oksidator | Korosif | Beracun | Bahaya Lingkungan",
        # GHS: GHS03 (oksidator), GHS05 (korosif), GHS06 (toksik), GHS09 (lingkungan)
        "wujud": "Padatan kristal putih transparan",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Fotoreaktif: terurai terkena cahaya menjadi Ag metalik (hitam) dan NOₓ; "
            "oksidator; bereaksi dengan klorida, bromida, iodida membentuk endapan AgX; "
            "meninggalkan noda hitam permanen pada kulit (Ag→AgO); "
            "korosif terhadap jaringan hidup; "
            "toksik bagi organisme akuatik; "
            "bereaksi dengan amonia pekat membentuk fulminating silver eksplosif — JANGAN dicampur"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca gelap berlabel "
            "'LIMBAH B3 – LOGAM MULIA – AgNO₃'. Simpan jauh dari cahaya.\n"
            "Langkah 2: JANGAN campur dengan bahan organik, klorida, atau amonia.\n"
            "Langkah 3: Endapkan Ag⁺ dengan NaCl → AgCl putih tidak larut; saring.\n"
            "Langkah 4: Serahkan endapan dan filtrat ke pengelola limbah B3 "
            "untuk daur ulang perak."
        ),
    },

    # ── KARBOHIDRAT ───────────────────────────────────────────────────
    "Glukosa": {
        "rumus": "C₆H₁₂O₆",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram bahaya
        "wujud": "Padatan kristal putih atau serbuk",
        "bau": "Sedikit manis",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "gula pereduksi (memiliki gugus aldehida bebas pada α-D-glukosa); "
            "mereduksi Cu²⁺ (reaksi Fehling, biru → merah bata Cu₂O); "
            "mereduksi Ag⁺ (reaksi Tollens, cermin perak); "
            "fermentasi oleh ragi menjadi etanol + CO₂; "
            "mengalami mutarotasi dalam larutan"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Sukrosa": {
        "rumus": "C₁₂H₂₂O₁₁",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram
        "wujud": "Padatan kristal putih",
        "bau": "Manis",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "bukan gula pereduksi (tidak memiliki gugus aldehida/keton bebas); "
            "terhidrolisis dalam asam encer membentuk glukosa dan fruktosa (gula invert); "
            "karamelisasi pada suhu >160°C"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },

    # ── SURFAKTAN & POLIMER ───────────────────────────────────────────
    "Sodium Dodesil Sulfat": {
        "rumus": "C₁₂H₂₅SO₄Na (SDS / Sodium Lauryl Sulfate)",
        # KOREKSI: rumus sebelumnya "SDS" tidak valid sebagai rumus kimia
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi kulit/mata)
        "wujud": "Serbuk putih atau granul",
        "bau": "Tidak berbau atau bau sabun lemah",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "anionik surfaktan kuat (menurunkan tegangan permukaan); "
            "denaturasi protein dengan memecah interaksi hidrofobik dan muatan (SDS-PAGE); "
            "membentuk misel di atas CMC (8 mM); "
            "bereaksi dengan garam logam divalen menghasilkan endapan tidak larut; "
            "iritasi kulit/mata pada konsentrasi tinggi"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan larutan SDS dalam wadah berlabel 'LIMBAH SURFAKTAN'.\n"
            "Langkah 2: Encerkan dengan air (1:10).\n"
            "Langkah 3: Netralisasi pH jika perlu.\n"
            "Langkah 4: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Polietilen Glikol": {
        "rumus": "H(OCH₂CH₂)ₙOH (PEG)",
        # KOREKSI: rumus "PEG" bukan rumus kimia
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram
        "wujud": "Cairan kental (PEG 200–600) atau padatan lilin (PEG >1000)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Sangat stabil pada suhu kamar; "
            "tidak reaktif terhadap asam/basa encer; "
            "larut dalam air dan banyak pelarut organik; "
            "bersifat higroskopis; "
            "inert secara biologis dan digunakan dalam farmasi/kosmetik"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah berlabel 'LIMBAH POLIMER'.\n"
            "Langkah 2: Jumlah kecil dapat dibuang ke saluran air.\n"
            "Langkah 3: Jumlah besar serahkan ke pengelola limbah."
        ),
    },
    "Polivinil Alkohol": {
        "rumus": "(C₂H₄O)ₙ (PVA)",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram
        "wujud": "Padatan putih atau granul",
        "bau": "Tidak berbau atau sedikit bau alkohol",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "larut dalam air panas (>80°C), tidak larut dalam pelarut organik umum; "
            "tidak reaktif dalam kondisi normal; "
            "dapat membentuk hidrogel dengan agen pengikat silang (boraks, glutaraldehid); "
            "higroskopis moderat"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },

    # ── SENYAWA REAKTIF/TOKSIK ORGANIK ───────────────────────────────
    "Akrilonitril": {
        "rumus": "CH₂=CHCN (C₃H₃N)",
        "simbol_bahaya": "Sangat Mudah Terbakar | Toksik | Karsinogen | Bahaya Lingkungan",
        # GHS: GHS02, GHS06, GHS08 (karsinogen Kel.1B), GHS09
        "wujud": "Cairan tidak berwarna",
        "bau": "Tajam khas menyengat (seperti peach)",
        "reaktivitas": (
            "Sangat mudah terbakar (titik nyala −1°C); "
            "berpolimerisasi eksotermis jika tanpa inhibitor (MEHQ/HQ); "
            "bereaksi dengan oksidator, asam, basa; "
            "toksik akut: LD₅₀ tikus oral = 78 mg/kg; "
            "karsinogen IARC Kelompok 1B (kanker paru pada pekerja); "
            "berbahaya bagi lingkungan akuatik"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah logam atau kaca tertutup rapat berlabel "
            "'LIMBAH B3 – TOKSIK KARSINOGEN REAKTIF'.\n"
            "Langkah 2: Hindari kontak langsung dan inhalasi — gunakan APD lengkap.\n"
            "Langkah 3: JANGAN campur dengan oksidator atau basa.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk pengolahan khusus."
        ),
    },
    "Formaldehid": {
        "rumus": "CH₂O (larutan formalin 37–40% dalam air)",
        "simbol_bahaya": "Mudah Terbakar | Beracun | Korosif | Karsinogen",
        # GHS: GHS02, GHS06, GHS05, GHS08 (karsinogen Kel.1A)
        "wujud": "Gas tidak berwarna (murni); larutan berair (formalin)",
        "bau": "Tajam sangat menyengat, asfiksia",
        "reaktivitas": (
            "Mudah terbakar (titik nyala formalin 50°C, gas formaldehid eksplosif 7–73%); "
            "bereaksi dengan protein melalui ikatan silang gugus amino (fiksasi jaringan); "
            "teroksidasi menjadi asam format di udara; "
            "berpolimerisasi membentuk paraformaldehid; "
            "karsinogen IARC Kelompok 1A (kanker nasofaring); "
            "sensitizer kulit dan saluran pernapasan; "
            "tidak kompatibel dengan HNO₃, oksidator kuat, fenol, amonia"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah HDPE atau kaca tertutup rapat berlabel "
            "'LIMBAH B3 – KARSINOGEN BERACUN'.\n"
            "Langkah 2: Hindari kontak langsung dan inhalasi — gunakan APD respirator.\n"
            "Langkah 3: Untuk volume kecil: oxidasi dengan KMnO₄ atau H₂O₂ encer "
            "mengubah formaldehid menjadi format.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk insinerasi."
        ),
    },
    "Glutaraldehid": {
        "rumus": "C₅H₈O₂ (OHC-(CH₂)₃-CHO, pentanedial)",
        "simbol_bahaya": "Beracun | Korosif | Bahaya Lingkungan",
        # GHS: GHS06 (toksik), GHS05 (korosif), GHS09 (lingkungan)
        "wujud": "Cairan tidak berwarna hingga kuning pucat",
        "bau": "Tajam khas menyengat",
        "reaktivitas": (
            "Daldehid bifungsional; bereaksi cepat dengan protein melalui ikatan silang "
            "gugus amino (lebih efisien dari formaldehid); "
            "disinfektan dan sterilant tingkat tinggi (aktif terhadap bakteri, spora, virus); "
            "lebih stabil dari formaldehid dalam kondisi alkali; "
            "sensitizer kulit dan saluran pernapasan kuat; "
            "toksik: LD₅₀ tikus oral = 250 mg/kg; "
            "sangat toksik bagi organisme akuatik"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik HDPE berlabel "
            "'LIMBAH B3 – TOKSIK DISINFEKTAN'.\n"
            "Langkah 2: Hindari kontak langsung dan inhalasi — gunakan APD.\n"
            "Langkah 3: Netralisasi dengan glisin (1% b/v) atau NaHSO₃ untuk "
            "menginaktivasi glutaraldehid sebelum pembuangan.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat."
        ),
    },
    "Fenol": {
        "rumus": "C₆H₅OH",
        "simbol_bahaya": "Beracun | Korosif",
        # GHS: GHS06 (toksik akut), GHS05 (korosif)
        "wujud": "Padatan kristal putih/merah muda (murni); cairan tidak berwarna di atas 40,9°C",
        "bau": "Khas manis-menyengat (bau karbol)",
        "reaktivitas": (
            "Asam lemah (pKa = 9,99); "
            "bereaksi dengan basa kuat membentuk garam fenolat (larut); "
            "substitusi elektrofilik aromatik 1000× lebih reaktif dari benzena; "
            "teroksidasi oleh udara menjadi warna merah-coklat; "
            "toksik dermik kuat: diserap melalui kulit, menyebabkan nekrosis; "
            "LD₅₀ tikus oral = 317 mg/kg; "
            "tidak kompatibel dengan oksidator kuat, basa kuat, asam nitrat"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca berlabel 'LIMBAH B3 – FENOL BERACUN'.\n"
            "Langkah 2: JANGAN campur dengan oksidator kuat.\n"
            "Langkah 3: Oksidasi dengan KMnO₄ atau H₂O₂ encer untuk mengurangi toksisitas.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat — "
            "JANGAN dibuang ke saluran umum."
        ),
    },
    "Anilina": {
        "rumus": "C₆H₅NH₂ (aminobenzena)",
        "simbol_bahaya": "Beracun | Bahaya Lingkungan",
        # GHS: GHS06 (toksik akut), GHS08 (toksik SSP/pembentuk methemoglobin), GHS09
        "wujud": "Cairan berminyak tidak berwarna (menjadi coklat di udara)",
        "bau": "Khas aromatik amis",
        "reaktivitas": (
            "Basa lemah (pKb = 9,38); bereaksi dengan asam membentuk garam anilinium; "
            "teroksidasi oleh udara menjadi produk berwarna coklat/hitam; "
            "diazotasi dengan HNO₂ pada suhu rendah → garam diazonium (prekursor zat warna azo); "
            "toksik: methemoglobinemia (mengoksidasi Hb menjadi MetHb, tidak bisa ikat O₂); "
            "LD₅₀ tikus oral = 442 mg/kg; "
            "diserap melalui kulit"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca atau HDPE berlabel 'LIMBAH B3 – TOKSIK'.\n"
            "Langkah 2: Hindari inhalasi dan kontak kulit — gunakan APD lengkap.\n"
            "Langkah 3: JANGAN campur dengan limbah lain.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk insinerasi suhu tinggi."
        ),
    },
    "Piridina": {
        "rumus": "C₅H₅N",
        "simbol_bahaya": "Mudah Terbakar | Beracun | Iritasi",
        # GHS: GHS02 (mudah terbakar), GHS07 (iritasi/toksik)
        "wujud": "Cairan tidak berwarna",
        "bau": "Menyengat kuat, seperti ikan/amis tidak sedap",
        "reaktivitas": (
            "Mudah terbakar (titik nyala 17°C); "
            "basa aromatic lemah (pKa konjugat asam = 5,23); "
            "bereaksi dengan asam membentuk garam piridinium; "
            "pelarut polar aprotik; menyerap air kuat (higroskopis); "
            "toksik: gangguan hati pada paparan kronis; "
            "tidak kompatibel dengan oksidator kuat, asam kuat"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah kaca atau logam berlabel 'LIMBAH B3 – TOKSIK'.\n"
            "Langkah 2: Hindari inhalasi dan kontak kulit — gunakan APD.\n"
            "Langkah 3: JANGAN campur dengan limbah lain.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk insinerasi."
        ),
    },

    # ── HIDROKARBON SIKLIK & SENYAWA ORGANIK KHUSUS ───────────────────
    "Sikloheksana": {
        "rumus": "C₆H₁₂",
        "simbol_bahaya": "Mudah Terbakar | Iritasi | Bahaya Lingkungan",
        # GHS: GHS02 (mudah terbakar), GHS07 (iritasi), GHS09 (bahaya lingkungan)
        "wujud": "Cairan tidak berwarna",
        "bau": "Khas minyak tanah",
        "reaktivitas": (
            "Mudah terbakar (titik nyala −18°C); "
            "stabil pada suhu kamar; "
            "tidak reaktif terhadap asam/basa encer; "
            "bereaksi substitusi radikal bebas dengan halogen di bawah UV; "
            "toksik bagi lingkungan; "
            "uap lebih berat dari udara"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah logam atau kaca berlabel "
            "'LIMBAH B3 – MUDAH TERBAKAR'.\n"
            "Langkah 2: Simpan di lemari asam, jauh dari api dan oksidator.\n"
            "Langkah 3: JANGAN buang ke saluran atau lingkungan.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat."
        ),
    },
    "Karbon Disulfida": {
        "rumus": "CS₂",
        "simbol_bahaya": "Sangat Mudah Terbakar | Beracun",
        # GHS: GHS02 (titik nyala −30°C!), GHS06 (toksik), GHS07 (iritasi)
        # KOREKSI: "autoignisi 90°C" adalah informasi kritis yang benar
        "wujud": "Cairan tidak berwarna (murni); kuning-kuning (teknis, bau busuk)",
        "bau": "Busuk seperti telur busuk (CS₂ teknis mengandung pengotor H₂S)",
        "reaktivitas": (
            "Sangat mudah terbakar (titik nyala −30°C; suhu autoignisi hanya 90°C); "
            "batas ledakan 1–50% — sangat lebar; "
            "uap lebih berat dari udara; "
            "bereaksi dengan oksidator, amina, nitrogen oksida; "
            "toksik SSP: menyebabkan neuropati perifer dan gangguan kardiovaskular; "
            "tidak kompatibel dengan logam alkali, oksidator, amina"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah logam atau kaca gelap berlabel "
            "'LIMBAH B3 – SANGAT MUDAH TERBAKAR BERACUN'.\n"
            "Langkah 2: Simpan di lemari asam jauh dari semua sumber api (termasuk nyala pilot, "
            "percikan listrik statik) — suhu autoignisi hanya 90°C!\n"
            "Langkah 3: JANGAN buang ke saluran atau tempat sampah.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 bersertifikat untuk insinerasi."
        ),
    },
    "Naftalena": {
        "rumus": "C₁₀H₈",
        "simbol_bahaya": "Mudah Terbakar | Beracun | Karsinogen | Bahaya Lingkungan",
        # GHS: GHS02, GHS07, GHS08 (karsinogen Cat.2), GHS09
        "wujud": "Padatan kristal putih",
        "bau": "Khas kapur barus (naftalena adalah bahan aktif kapur barus lama)",
        "reaktivitas": (
            "Mudah terbakar; "
            "menyublim perlahan pada suhu kamar (tekanan uap signifikan); "
            "bereaksi substitusi elektrofilik lebih mudah dari benzena; "
            "teroksidasi oleh KMnO₄/O₂ menghasilkan asam ftalat; "
            "karsinogen Cat.2 GHS; toksik bagi sel darah merah (hemolisis); "
            "sangat toksik bagi organisme akuatik"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan padatan dalam wadah tertutup rapat berlabel "
            "'LIMBAH B3 – MUDAH TERBAKAR TOKSIK'. Wadah harus kedap udara karena menyublim.\n"
            "Langkah 2: Simpan di area sejuk dan berventilasi.\n"
            "Langkah 3: JANGAN buang ke saluran atau lingkungan.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 untuk insinerasi."
        ),
    },
    "Asam Benzoat": {
        "rumus": "C₇H₆O₂",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi)
        "wujud": "Padatan kristal putih bersisik",
        "bau": "Khas aromatik lemah (bau almond)",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "asam lemah (pKa = 4,19); "
            "bereaksi dengan basa membentuk garam benzoat (larut); "
            "dapat menyublim pada suhu tinggi; "
            "bersifat antimikroba (menghambat pertumbuhan jamur/bakteri) pada pH rendah; "
            "tidak kompatibel dengan oksidator kuat"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah dalam wadah plastik atau kaca berlabel "
            "'LIMBAH ASAM LEMAH'.\n"
            "Langkah 2: Encerkan dengan air (1:5).\n"
            "Langkah 3: Netralisasi dengan NaHCO₃ atau NaOH encer hingga pH 6–8.\n"
            "Langkah 4: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },

    # ── GAS ────────────────────────────────────────────────────────────
    "Metana": {
        "rumus": "CH₄",
        "simbol_bahaya": "Sangat Mudah Terbakar | Gas Bertekanan",
        # GHS: GHS02 (mudah terbakar), GHS04 (gas bertekanan)
        "wujud": "Gas tidak berwarna",
        "bau": "Tidak berbau (murni); bau merkaptan ditambahkan sebagai penanda kebocoran pada gas alam",
        # KOREKSI: gas alam beraroma karena penambahan merkaptan, bukan metana murni
        "reaktivitas": (
            "Sangat mudah terbakar (batas ledakan 5–15% v/v di udara); "
            "terbakar dengan nyala biru; "
            "bereaksi substitusi radikal bebas dengan halogen di bawah UV; "
            "gas rumah kaca (GWP 21×CO₂); "
            "lebih ringan dari udara; stabil secara kimia dalam kondisi normal"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Biarkan menguap di area berventilasi tinggi dalam jumlah kecil.\n"
            "Langkah 2: JANGAN buang ke saluran tertutup (risiko ledakan).\n"
            "Langkah 3: Untuk jumlah besar — serahkan ke pengelola limbah gas.\n"
            "Langkah 4: Pastikan tidak ada api, percikan, atau elektrostatik di area penanganan."
        ),
    },
    "Propana": {
        "rumus": "C₃H₈",
        "simbol_bahaya": "Sangat Mudah Terbakar | Gas Bertekanan",
        # GHS: GHS02, GHS04
        "wujud": "Gas tidak berwarna (atau cairan bertekanan dalam tabung)",
        "bau": "Tidak berbau (murni); bau merkaptan ditambahkan dalam LPG",
        "reaktivitas": (
            "Sangat mudah terbakar (batas ledakan 2,1–9,5% v/v di udara); "
            "lebih berat dari udara; "
            "terbakar menghasilkan CO₂ dan H₂O; "
            "bereaksi substitusi radikal bebas dengan halogen; "
            "komponen utama LPG; "
            "asfiksia sederhana pada konsentrasi tinggi"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Biarkan menguap di area berventilasi tinggi dalam jumlah kecil.\n"
            "Langkah 2: JANGAN buang ke saluran tertutup atau cekungan rendah "
            "(gas lebih berat dari udara — risiko ledakan).\n"
            "Langkah 3: Untuk jumlah besar — serahkan ke pengelola limbah gas.\n"
            "Langkah 4: Pastikan tidak ada sumber pengapian."
        ),
    },
    "Butana": {
        "rumus": "C₄H₁₀",
        "simbol_bahaya": "Sangat Mudah Terbakar | Gas Bertekanan",
        # GHS: GHS02, GHS04
        "wujud": "Gas tidak berwarna (atau cairan bertekanan dalam tabung/kaleng)",
        "bau": "Tidak berbau (murni); bau merkaptan dalam LPG",
        "reaktivitas": (
            "Sangat mudah terbakar (batas ledakan 1,8–8,4% v/v di udara); "
            "lebih berat dari udara; "
            "komponen LPG (bersama propana); "
            "bereaksi substitusi halogenasi dengan UV; "
            "asfiksia sederhana pada konsentrasi tinggi"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Biarkan menguap di area berventilasi tinggi dalam jumlah kecil.\n"
            "Langkah 2: JANGAN buang ke saluran tertutup atau cekungan rendah.\n"
            "Langkah 3: Untuk jumlah besar — serahkan ke pengelola limbah gas.\n"
            "Langkah 4: Pastikan tidak ada sumber pengapian."
        ),
    },
    "Etena": {
        "rumus": "C₂H₄ (etilena)",
        "simbol_bahaya": "Sangat Mudah Terbakar | Gas Bertekanan",
        # GHS: GHS02, GHS04
        "wujud": "Gas tidak berwarna",
        "bau": "Khas sedikit manis (pada konsentrasi tinggi)",
        "reaktivitas": (
            "Sangat mudah terbakar (batas ledakan 2,7–36% v/v di udara); "
            "bereaksi adisi elektrofilik: halogenasi (+ Br₂ → 1,2-dibromoetana, "
            "uji alkena dekolorisasi Br₂/KMnO₄); "
            "polimerisasi menjadi polietilena dengan katalis Ziegler-Natta; "
            "hormon pertumbuhan tanaman alami; "
            "asfiksia sederhana pada konsentrasi tinggi"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Biarkan menguap di area berventilasi tinggi dalam jumlah kecil.\n"
            "Langkah 2: JANGAN buang ke saluran tertutup (risiko ledakan).\n"
            "Langkah 3: Untuk jumlah besar — serahkan ke pengelola limbah gas.\n"
            "Langkah 4: Pastikan tidak ada sumber pengapian."
        ),
    },
    "Asetilena": {
        "rumus": "C₂H₂ (etuna)",
        "simbol_bahaya": "Sangat Mudah Terbakar | Eksplosif | Gas Bertekanan",
        # GHS: GHS02 (sangat mudah terbakar), GHS01 (eksplosif), GHS04 (gas bertekanan)
        "wujud": "Gas tidak berwarna",
        "bau": "Khas eter-aromatik (teknis: sedikit bau bawang putih dari pengotor PH₃/AsH₃)",
        "reaktivitas": (
            "Sangat mudah terbakar (titik nyala −18°C, batas ledakan 2,5–80% — sangat lebar); "
            "nyala asetilena-oksigen mencapai 3.100–3.500°C (las); "
            "dapat meledak pada tekanan >1,5 atm tanpa pelarut; "
            "disimpan terlarut dalam aseton dalam silinder berpori; "
            "membentuk asetilida eksplosif dengan logam Cu, Ag, Hg "
            "— JANGAN gunakan komponen tembaga atau perak!"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Gas sisa biarkan menguap di area berventilasi tinggi.\n"
            "Langkah 2: JANGAN buang ke saluran tertutup.\n"
            "Langkah 3: Silinder kosong kembalikan ke supplier — jangan buang sendiri.\n"
            "Langkah 4: JAUHKAN dari logam Cu dan Ag — asetilida eksplosif."
        ),
    },

    # ── LOGAM UNSUR ────────────────────────────────────────────────────
    "Magnesium": {
        "rumus": "Mg",
        "simbol_bahaya": "Mudah Terbakar | Bereaksi dengan Air",
        # GHS: GHS02 (serbuk mudah terbakar), GHS07 (iritasi)
        "wujud": "Padatan metalik perak-putih (lempengan, kawat, pita, atau serbuk)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Serbuk dan pita Mg mudah terbakar dengan nyala putih sangat terang (buta); "
            "bereaksi dengan asam encer (HCl, H₂SO₄, CH₃COOH) menghasilkan gas H₂; "
            "bereaksi dengan air panas/uap menghasilkan Mg(OH)₂ + H₂; "
            "serbuk halus dapat bereaksi spontan dengan air dingin; "
            "tidak kompatibel dengan oksidator kuat, halogen, karbon dioksida "
            "(CO₂ tidak bisa memadamkan nyala Mg!)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan padatan Mg dalam wadah kering berlabel "
            "'LIMBAH LOGAM REAKTIF – Mg'. JANGAN campur dengan air.\n"
            "Langkah 2: Simpan di tempat kering, jauh dari api dan air.\n"
            "Langkah 3: JANGAN gunakan CO₂ atau air sebagai pemadam; gunakan pasir kering.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 atau daur ulang logam."
        ),
    },
    "Aluminium": {
        "rumus": "Al",
        "simbol_bahaya": "Mudah Terbakar (serbuk) | Reaktif dengan Basa/Asam",
        # GHS: GHS02 untuk serbuk halus; bulk tidak berbahaya signifikan
        # KOREKSI: "Tidak berbahaya" untuk Al bulk sudah benar, tapi serbuk Al termasuk mudah terbakar
        "wujud": "Padatan metalik perak-mengkilap (bulk); serbuk/foil abu-abu (serbuk)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Membentuk lapisan oksida Al₂O₃ pasif di udara (perlindungan korosi); "
            "amfoter: bereaksi dengan asam kuat (HCl, H₂SO₄) DAN basa kuat (NaOH, KOH) "
            "menghasilkan gas H₂; "
            "serbuk aluminium mudah terbakar dan merupakan bahan piroteknik; "
            "bereaksi dengan oksidator kuat secara eksotermis"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan padatan/logam dalam wadah kering berlabel 'LIMBAH LOGAM'.\n"
            "Langkah 2: JANGAN campur dengan asam atau basa kuat (risiko H₂).\n"
            "Langkah 3: Serbuk Al — beri label 'MUDAH TERBAKAR', jauhkan dari api.\n"
            "Langkah 4: Serahkan ke pengelola daur ulang logam."
        ),
    },
    "Besi": {
        "rumus": "Fe",
        "simbol_bahaya": "Tidak Berbahaya (bulk) | Mudah Terbakar (serbuk halus)",
        # GHS: tidak ada untuk bulk; GHS02 untuk serbuk piroforik
        "wujud": "Padatan metalik abu-abu (bulk) atau serbuk hitam-abu (serbuk)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Berkarat (teroksidasi membentuk Fe₂O₃·nH₂O) di udara lembab; "
            "bereaksi lambat dengan asam encer (HCl, H₂SO₄) menghasilkan Fe²⁺ + H₂; "
            "tidak bereaksi dengan basa; "
            "serbuk Fe halus dapat bersifat piroforik; "
            "magnetis"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan padatan dalam wadah kering berlabel 'LIMBAH LOGAM'.\n"
            "Langkah 2: Keringkan dan serahkan ke pengelola daur ulang logam.\n"
            "Langkah 3: Serbuk halus — beri label 'MUDAH TERBAKAR', simpan kering."
        ),
    },
    "Tembaga": {
        "rumus": "Cu",
        "simbol_bahaya": "Bahaya Lingkungan (debu/serbuk)",
        # GHS: GHS09 untuk debu/serbuk (toksik akuatik)
        "wujud": "Padatan metalik merah-jingga mengkilap",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Tidak bereaksi dengan air atau asam non-oksidator HCl encer; "
            "bereaksi dengan HNO₃ menghasilkan gas NOₓ; "
            "bereaksi dengan H₂SO₄ panas menghasilkan SO₂; "
            "membentuk patina hijau (CuCO₃·Cu(OH)₂) di udara lembab; "
            "debu/serbuk toksik bagi organisme akuatik; "
            "tahan korosi dalam kondisi normal"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan padatan dalam wadah kering berlabel 'LIMBAH LOGAM – Cu'.\n"
            "Langkah 2: Keringkan dan serahkan ke pengelola daur ulang logam.\n"
            "Langkah 3: JANGAN buang debu Cu ke perairan — toksik akuatik."
        ),
    },
    "Timbal": {
        "rumus": "Pb",
        "simbol_bahaya": "Beracun | Bahaya Reproduksi | Bahaya Lingkungan",
        # GHS: GHS06 (toksik akut), GHS08 (toksik reproduksi Cat.1A, neurotoksik), GHS09
        "wujud": "Padatan metalik abu-abu kehitaman, lunak dan berat",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Tahan korosi dalam kondisi normal (lapisan PbO/PbCO₃ pasif); "
            "bereaksi lambat dengan asam kuat (HNO₃, HCl panas) menghasilkan Pb²⁺; "
            "tidak bereaksi dengan basa; "
            "sangat toksik dan bioakumulatif: timbal terakumulasi di tulang, "
            "menyebabkan gangguan otak pada anak (neurotoksik); "
            "karsinogen manusia; teratogenik (merusak janin)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik HDPE berlabel "
            "'LIMBAH LOGAM BERAT BERACUN – Pb'.\n"
            "Langkah 2: JANGAN campur dengan asam kuat (dapat melarutkan Pb).\n"
            "Langkah 3: Serahkan ke pengelola limbah B3 bersertifikat untuk daur ulang timbal.\n"
            "Langkah 4: JANGAN buang ke lingkungan — bioakumulatif dan sangat toksik."
        ),
    },

    # ── SENYAWA ANORGANIK LAINNYA ─────────────────────────────────────
    "Amonium Hidroksida": {
        "rumus": "NH₃(aq) / NH₄OH",
        # KOREKSI: NH₄OH tidak eksis sebagai spesies; lebih tepat NH₃ terlarut dalam air
        "simbol_bahaya": "Korosif | Iritasi | Beracun",
        # GHS: GHS05 (korosif), GHS07 (iritasi), GHS06 (toksik pada konsentrasi tinggi)
        "wujud": "Larutan berair tidak berwarna",
        "bau": "Sangat menyengat (gas amonia terlepas)",
        "reaktivitas": (
            "Larutan amonia dalam air; basa lemah (pKb = 4,74); "
            "melepaskan gas NH₃ jika dipanaskan atau ditambah basa kuat; "
            "bereaksi dengan asam membentuk garam amonium; "
            "membentuk kompleks amina dengan ion logam transisi; "
            "korosif terhadap Cu, Zn, dan paduan tembaga; "
            "iritasi kuat pada mata dan saluran pernapasan"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kerjakan di lemari asam berventilasi.\n"
            "Langkah 2: Kumpulkan limbah dalam wadah HDPE tertutup rapat berlabel "
            "'LIMBAH BASA – AMONIA'.\n"
            "Langkah 3: Encerkan dengan air (1:5).\n"
            "Langkah 4: Netralisasi dengan HCl encer hingga pH 6–8.\n"
            "Langkah 5: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Barium Hidroksida": {
        "rumus": "Ba(OH)₂",
        "simbol_bahaya": "Beracun | Korosif",
        # GHS: GHS06 (toksik akut), GHS05 (korosif)
        "wujud": "Padatan putih (oktahidrat atau anhidrat)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Basa kuat moderat; bereaksi dengan asam membentuk garam barium (eksotermis); "
            "menyerap CO₂ dari udara membentuk BaCO₃ (putih); "
            "bereaksi dengan Al dan Zn menghasilkan H₂; "
            "larutan basa kuat; toksik: Ba²⁺ menyebabkan hipokalemia; "
            "LD₅₀ tikus oral = 255 mg/kg"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik berlabel 'LIMBAH LOGAM BERAT – Ba'.\n"
            "Langkah 2: JANGAN campur dengan asam sulfat (endapan BaSO₄ mempersulit pengolahan).\n"
            "Langkah 3: Serahkan ke pengelola limbah B3 untuk pengolahan khusus.\n"
            "Langkah 4: JANGAN buang ke lingkungan — barium toksik bagi organisme."
        ),
    },
    "Litium Hidroksida": {
        "rumus": "LiOH",
        "simbol_bahaya": "Korosif | Beracun",
        # GHS: GHS05 (korosif), GHS07 (iritasi)
        "wujud": "Padatan putih (monohidrat atau anhidrat)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Basa kuat; bereaksi eksotermis dengan asam; "
            "menyerap CO₂ dari udara membentuk Li₂CO₃; "
            "higroskopis kuat; "
            "bereaksi dengan Al dan Zn menghasilkan H₂; "
            "toksik: Li⁺ toksik pada dosis >0,5 mEq/L serum; "
            "digunakan dalam baterai Li-ion dan pengolahan gas CO₂ di kapal selam"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah dalam wadah HDPE berlabel 'LIMBAH B3 – BASA KUAT'.\n"
            "Langkah 2: Netralisasi perlahan dengan HCl 10% sambil diaduk hingga pH 6–8.\n"
            "Langkah 3: Encerkan dengan air (1:10).\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 — Li adalah logam yang dikelola khusus."
        ),
    },

    # ── ASAM ORGANIK LAINNYA ──────────────────────────────────────────
    "Asam Sitrat": {
        "rumus": "C₆H₈O₇",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi)
        "wujud": "Padatan kristal putih atau serbuk",
        "bau": "Tidak berbau (sedikit bau asam pada konsentrasi tinggi)",
        "reaktivitas": (
            "Asam trikarboksilat (pKa₁=3,13; pKa₂=4,76; pKa₃=6,40); "
            "bereaksi dengan basa membentuk garam sitrat (buffer biologis penting); "
            "agen pengkhelat untuk ion logam (Ca²⁺, Mg²⁺, Fe³⁺); "
            "terurai pada suhu >175°C menjadi akonitik/itakonat; "
            "tidak mudah terbakar; terjadi alami dalam buah sitrus"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik berlabel 'LIMBAH ASAM LEMAH'.\n"
            "Langkah 2: Encerkan dengan air (1:5).\n"
            "Langkah 3: Netralisasi dengan NaHCO₃ atau NaOH encer hingga pH 6–8.\n"
            "Langkah 4: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Asam Format": {
        "rumus": "HCOOH (asam metanoat)",
        "simbol_bahaya": "Mudah Terbakar | Beracun | Korosif",
        # GHS: GHS02 (mudah terbakar), GHS06 (toksik), GHS05 (korosif)
        "wujud": "Cairan tidak berwarna",
        "bau": "Menyengat, bau khas semut/bahan pengawet",
        "reaktivitas": (
            "Asam karboksilat terkuat suku pertama (pKa = 3,75); "
            "mudah terbakar (titik nyala 50°C); "
            "bereaksi dengan basa membentuk garam format; "
            "reduktor (dapat mereduksi Ag⁺ menjadi cermin perak); "
            "terdekomposisi pada suhu tinggi menjadi CO + H₂O; "
            "toksik: menyebabkan asidosis metabolik; "
            "korosif terhadap kulit/mata/logam"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik atau kaca berlabel "
            "'LIMBAH B3 – ASAM MUDAH TERBAKAR'.\n"
            "Langkah 2: Encerkan dengan air (1:5).\n"
            "Langkah 3: Netralisasi dengan NaHCO₃ atau NaOH encer hingga pH 6–8.\n"
            "Langkah 4: Buang ke saluran pembuangan. Konsentrasi pekat: serahkan ke pengelola B3."
        ),
    },
    "Asam Oksalat": {
        "rumus": "H₂C₂O₄ (asam etanedioat)",
        "simbol_bahaya": "Beracun | Iritasi",
        # GHS: GHS06 (toksik akut oral), GHS07 (iritasi)
        "wujud": "Padatan kristal putih (dihidrat atau anhidrat)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Asam dikarboksilat (pKa₁=1,25; pKa₂=4,27); "
            "bereaksi dengan basa membentuk garam oksalat; "
            "mengkhelat Ca²⁺ membentuk kalsium oksalat tidak larut (CaC₂O₄); "
            "reduktor: dioksidasi oleh KMnO₄ (perubahan warna ungu → tak berwarna, "
            "digunakan dalam titrasi permanganometri); "
            "toksik: menyebabkan hipokalsemia dan kerusakan ginjal; "
            "LD₅₀ tikus oral = 375 mg/kg"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik atau kaca berlabel "
            "'LIMBAH ASAM LEMAH – TOKSIK'.\n"
            "Langkah 2: Encerkan dengan air (1:5).\n"
            "Langkah 3: Netralisasi dengan NaHCO₃ atau NaOH encer hingga pH 6–8.\n"
            "Langkah 4: Buang ke saluran pembuangan. Jangan dalam jumlah besar ke perairan."
        ),
    },
    "Asam Borat": {
        "rumus": "H₃BO₃",
        "simbol_bahaya": "Beracun | Iritasi | Bahaya Reproduksi",
        # GHS: GHS07 (iritasi), GHS08 (bahaya reproduksi Cat.1B/2)
        # KOREKSI: asam borat termasuk bahaya reproduksi berdasarkan GHS terbaru
        "wujud": "Padatan kristal putih bersisik",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Asam Lewis lemah (pKa = 9,24); "
            "bereaksi dengan alkohol (gliserin, sorbitol) membentuk kompleks ester borat; "
            "memberikan nyala hijau pada uji nyala api (emisi B); "
            "bersifat antiseptik dan insektisida ringan; "
            "toksik reproduktif (merusak sistem reproduksi); "
            "toksik kumulatif jika tertelan dalam jangka panjang"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik atau kaca berlabel "
            "'LIMBAH B3 – ASAM TOKSIK REPRODUKSI'.\n"
            "Langkah 2: Encerkan dengan air (1:5).\n"
            "Langkah 3: Netralisasi dengan NaHCO₃ atau NaOH encer hingga pH 6–8.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 — jangan dibuang besar-besaran "
            "ke perairan (bahaya reproduksi)."
        ),
    },
    "Asam Laktat": {
        "rumus": "C₃H₆O₃ (asam 2-hidroksipropanoat)",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi, terutama konsentrasi tinggi)
        "wujud": "Cairan kental tidak berwarna hingga kuning pucat",
        "bau": "Bau asam lemah",
        "reaktivitas": (
            "Asam hidroksikarboksilat (pKa = 3,86); "
            "stabil pada suhu kamar; "
            "bereaksi dengan basa membentuk garam laktat; "
            "teroksidasi menjadi asam piruvat; "
            "higroskopis; "
            "produk fermentasi bakteri asam laktat; biokompatibel"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik berlabel 'LIMBAH ASAM LEMAH'.\n"
            "Langkah 2: Encerkan dengan air (1:5).\n"
            "Langkah 3: Netralisasi dengan NaHCO₃ atau NaOH encer hingga pH 6–8.\n"
            "Langkah 4: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Asam Tartarat": {
        "rumus": "C₄H₆O₆ (asam L-tartarat)",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi ringan)
        "wujud": "Padatan kristal putih",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Asam dikarboksilat (pKa₁=2,89; pKa₂=4,40); "
            "stabil pada suhu kamar; "
            "bereaksi dengan basa membentuk tartrat; "
            "membentuk KHC₄H₄O₆ (cream of tartar) dengan K⁺; "
            "mengkhelat ion logam; "
            "terjadi alami dalam anggur dan asam jawa"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik berlabel 'LIMBAH ASAM LEMAH'.\n"
            "Langkah 2: Encerkan dengan air (1:5).\n"
            "Langkah 3: Netralisasi dengan NaHCO₃ atau NaOH encer hingga pH 6–8.\n"
            "Langkah 4: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },

    # ── SENYAWA BIOKIMIA & ANALITIK KHUSUS ───────────────────────────
    "Kurkumin": {
        "rumus": "C₂₁H₂₀O₆",
        "simbol_bahaya": "Iritasi (kurang berbahaya)",
        # GHS: tidak ada piktogram bahaya signifikan
        "wujud": "Serbuk kristal kuning-jingga",
        "bau": "Khas kunyit (aromatik, sedikit pedas)",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "indikator pH alami: kuning pada kondisi asam, merah-coklat pada basa; "
            "antioksidan (menangkap radikal bebas); "
            "sensitif terhadap cahaya UV (fotodegradasi); "
            "membentuk kompleks berwarna dengan ion logam (Fe³⁺, Cu²⁺); "
            "larut baik dalam etanol dan aseton, kurang larut dalam air"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah cair dalam wadah kaca berlabel "
            "'LIMBAH INDIKATOR ALAMI'.\n"
            "Langkah 2: Encerkan dengan air (1:10).\n"
            "Langkah 3: Buang ke saluran pembuangan. "
            "Konsentrasi pekat: serahkan ke pengelola limbah B3."
        ),
    },
    "Asam Sulfanilat": {
        "rumus": "C₆H₇NO₃S (asam 4-aminobenzensulfonat)",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi)
        "wujud": "Padatan kristalin putih hingga abu-abu (zwitterion)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Zwitterion (gugus -NH₃⁺ dan -SO₃⁻); "
            "stabil pada suhu kamar; "
            "bereaksi dengan basa membentuk garam sulfanilat; "
            "dapat mengalami diazotasi dengan HNO₂ dingin → garam diazonium "
            "(prekursor zat warna azo); "
            "larut dalam air panas dan basa encer"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik atau kaca berlabel "
            "'LIMBAH ASAM LEMAH'.\n"
            "Langkah 2: Encerkan dengan air (1:5).\n"
            "Langkah 3: Netralisasi dengan NaHCO₃ atau NaOH encer hingga pH 6–8.\n"
            "Langkah 4: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Kristal Violet": {
        "rumus": "C₂₅H₃₀ClN₃ (Gentian Violet)",
        "simbol_bahaya": "Iritasi | Karsinogen (Mungkin)",
        # GHS: GHS07 (iritasi), GHS08 (karsinogen Cat.2 berdasarkan beberapa regulasi)
        # KOREKSI: Crystal Violet perlu perbaikan rumus — C₂₅H₃₀ClN₃ (MW 407,99)
        "wujud": "Padatan kristal ungu gelap",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "pewarna triarilmetan (triphenylmethane dye); "
            "bereaksi dengan asam kuat membentuk warna hijau/kuning (perubahan muatan); "
            "antimikroba terhadap bakteri Gram-positif; "
            "karsinogen Cat.2 pada beberapa regulasi; "
            "digunakan dalam pewarnaan Gram bakteri"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah larutan dalam wadah kaca berlabel "
            "'LIMBAH B3 – PEWARNA/INDIKATOR'.\n"
            "Langkah 2: Encerkan dengan air (1:10).\n"
            "Langkah 3: Serahkan limbah pekat ke pengelola limbah B3."
        ),
    },
    "Alizarin Merah": {
        "rumus": "C₁₄H₈O₄ (Alizarin Red S: C₁₄H₇NaO₇S)",
        # KOREKSI: Alizarin free acid vs Alizarin Red S berbeda
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi)
        "wujud": "Serbuk merah-jingga hingga coklat",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "indikator pH (kuning pada pH <5,5; merah pada pH >6,8); "
            "membentuk kompleks berwarna dengan ion logam (Ca²⁺, Al³⁺, Fe³⁺) — "
            "digunakan dalam uji histokimia tulang (Alizarin Red S mendeteksi kalsium); "
            "pewarna mordant anthraquinone"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan limbah larutan dalam wadah kaca berlabel "
            "'LIMBAH B3 – INDIKATOR/PEWARNA'.\n"
            "Langkah 2: Encerkan dengan air (1:10).\n"
            "Langkah 3: Serahkan limbah pekat ke pengelola limbah B3."
        ),
    },

    # ── SENYAWA NITROGEN ──────────────────────────────────────────────
    "Amonium Sulfat": {
        "rumus": "(NH₄)₂SO₄",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi)
        "wujud": "Padatan kristal putih",
        "bau": "Tidak berbau (sedikit bau amonia jika lembab)",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "bereaksi dengan basa kuat menghasilkan gas NH₃; "
            "larut dalam air (endotermis); "
            "terurai pada suhu >280°C melepaskan NH₃ dan SO₃; "
            "digunakan sebagai pupuk nitrogen-sulfur dan dalam pengendapan protein "
            "(salting-out)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Netralisasi pH jika perlu hingga 6–8.\n"
            "Langkah 3: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Natrium Fosfat": {
        "rumus": "Na₃PO₄ (trinatrium fosfat)",
        "simbol_bahaya": "Iritasi | Korosif",
        # GHS: GHS07 (iritasi), GHS05 (korosif — pH larutan ~12,5)
        # KOREKSI: Na₃PO₄ adalah basa kuat dalam larutan (pH ~12), perlu tambahan korosif
        "wujud": "Padatan putih (anhidrat atau dodekahodrat)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Basa kuat dalam larutan (pH 1% ≈ 12,5); "
            "bereaksi dengan asam membentuk garam fosfat (netralisasi); "
            "bereaksi dengan ion logam berat membentuk endapan fosfat tidak larut; "
            "digunakan sebagai buffer, pembersih, dan agen sekuestran; "
            "korosif terhadap kulit dan mata pada konsentrasi tinggi"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik berlabel 'LIMBAH BASA'.\n"
            "Langkah 2: Encerkan dengan air minimal 1:10.\n"
            "Langkah 3: Netralisasi dengan HCl encer hingga pH 6–8.\n"
            "Langkah 4: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },

    # ── SENYAWA ORGANIK LAINNYA ───────────────────────────────────────
    "Urea": {
        "rumus": "CO(NH₂)₂",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram
        "wujud": "Padatan kristal putih atau granul",
        "bau": "Tidak berbau (sedikit bau amonia jika terurai)",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "terhidrolisis lambat dalam air menjadi NH₃ dan CO₂ (dipercepat oleh urease); "
            "terurai pada suhu >133°C (titik leleh sekaligus dekomposisi); "
            "bereaksi dengan asam membentuk garam urea; "
            "denaturan protein pada konsentrasi tinggi (6–8 M); "
            "pupuk nitrogen dengan kandungan N tertinggi (46%)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir. "
            "Tidak diperlukan penanganan B3 khusus."
        ),
    },
    "Asam Urat": {
        "rumus": "C₅H₄N₄O₃ (2,6,8-trioksipurina)",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram
        "wujud": "Padatan kristal putih",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "sangat sukar larut dalam air (0,15 mg/mL); "
            "bereaksi dengan basa membentuk garam urat; "
            "produk akhir metabolisme purin pada manusia; "
            "membentuk kristal monosodium urat pada hiperurisemia (gout); "
            "tidak mudah terbakar"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },

    # ── MATERIAL/BAHAN PENDUKUNG ──────────────────────────────────────
    "Air": {
        "rumus": "H₂O",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        "wujud": "Cairan tidak berwarna",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Sangat stabil; pelarut universal; "
            "bereaksi eksotermis dengan logam alkali (Na, K) dan alkali tanah (Ca) "
            "menghasilkan OH⁻ + H₂; "
            "hidrolisis banyak garam dan senyawa; "
            "tidak beracun, tidak mudah terbakar"
        ),
        "pengelolaan_limbah": (
            "Buang langsung ke saluran pembuangan. "
            "Air laboratorium yang terkontaminasi bahan lain harus diperlakukan "
            "sesuai sifat kontaminannya."
        ),
    },
    "Karbon Aktif": {
        "rumus": "C (karbon amorf berpori)",
        "simbol_bahaya": "Tidak Berbahaya | Mudah Terbakar (serbuk halus)",
        # GHS: GHS02 untuk serbuk karbon aktif halus (debu mudah terbakar)
        "wujud": "Serbuk atau granul hitam",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Sangat stabil secara kimia; "
            "mengadsorpsi gas, molekul organik, dan ion (fisiosorpsi dan kemosorpsi); "
            "serbuk halus dapat membentuk debu eksplosif; "
            "inert terhadap asam/basa encer; "
            "dapat diregenerasi dengan pemanasan 500–800°C dalam atmosfer inert"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah tertutup berlabel sesuai kontaminannya.\n"
            "Langkah 2: Karbon aktif dapat diregenerasi dengan pemanasan.\n"
            "Langkah 3: Jika terkontaminasi zat berbahaya, perlakukan sesuai sifat kontaminan.\n"
            "Langkah 4: Buang ke tempat sampah umum jika bersih."
        ),
    },
    "Silika Gel": {
        "rumus": "SiO₂·nH₂O (amorf)",
        "simbol_bahaya": "Iritasi (debu silikosis)",
        # GHS: GHS07 (iritasi paru-debu)
        # KOREKSI: silika gel berpotensi iritan paru jika dihirup (debu)
        "wujud": "Padatan putih atau transparan (granul, manik, atau bead)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Higroskopis kuat (dapat menyerap hingga 40% beratnya sendiri sebagai air); "
            "stabil pada suhu kamar; inert terhadap asam dan basa encer; "
            "bereaksi dengan HF membentuk SiF₄; "
            "dapat diregenerasi dengan pemanasan 120–150°C; "
            "debu inhalasi kronik berisiko silikosis (amorf, bukan kristal — risiko lebih rendah)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah tertutup.\n"
            "Langkah 2: Jika terkontaminasi, perlakukan sesuai kontaminannya.\n"
            "Langkah 3: Buang ke tempat sampah umum jika bersih."
        ),
    },
    "Mineral Oil": {
        "rumus": "Campuran alkana C₁₅–C₄₀ (parafin mineral)",
        # KOREKSI: rumus sebelumnya "Mineral oil" bukan rumus kimia
        "simbol_bahaya": "Iritasi (kabut/aerosol)",
        # GHS: GHS07 (iritasi paru dari kabut/aerosol)
        # KOREKSI: "Tidak berbahaya" kurang tepat — mineral oil kabut berpotensi karsinogen
        "wujud": "Cairan kental tidak berwarna hingga putih susu",
        "bau": "Tidak berbau atau bau minyak sangat lemah",
        "reaktivitas": (
            "Sangat stabil; inert secara kimia terhadap asam/basa encer; "
            "tidak mudah terbakar pada suhu kamar (titik nyala >100°C); "
            "melarutkan senyawa non-polar; "
            "kabut/aerosol mineral oil dalam industri: karsinogen IARC Kelompok 1 "
            "(kanker kulit); "
            "food-grade mineral oil aman untuk konsumsi"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah berlabel 'LIMBAH MINYAK'.\n"
            "Langkah 2: Jumlah kecil: serap dengan absorben (pasir/serbuk gergaji), "
            "buang ke tempat sampah.\n"
            "Langkah 3: Jumlah besar: serahkan ke pengelola limbah minyak."
        ),
    },
    "Gliserol": {
        "rumus": "C₃H₈O₃ (gliserin, propan-1,2,3-triol)",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram
        "wujud": "Cairan kental tidak berwarna",
        "bau": "Manis lemah",
        "reaktivitas": (
            "Sangat stabil pada suhu kamar; "
            "higroskopis kuat; "
            "bereaksi dengan asam karboksilat membentuk ester (gliserida — komponen lemak); "
            "teroksidasi oleh oksidator kuat menjadi gliseraldehida dan dihidroksiaseton; "
            "larut sempurna dalam air; tidak beracun (LD₅₀ tikus oral >12 g/kg)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
    "Asam Oleat": {
        "rumus": "C₁₈H₃₄O₂ (asam cis-9-oktadekenoat)",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi)
        "wujud": "Cairan kental kuning pucat (cair di atas 13,4°C)",
        "bau": "Bau lemak/minyak khas",
        "reaktivitas": (
            "Stabil pada suhu kamar dalam kondisi normal; "
            "asam lemak tak jenuh tunggal (satu ikatan rangkap C9=C10 cis); "
            "teroksidasi oleh udara perlahan (ketengikan); "
            "bereaksi dengan basa membentuk sabun (saponifikasi); "
            "hidrogenasi menghasilkan asam stearat; "
            "tidak mudah terbakar dalam kondisi normal"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah berlabel 'LIMBAH MINYAK/LEMAK'.\n"
            "Langkah 2: Jumlah kecil: serap dengan absorben, buang ke tempat sampah.\n"
            "Langkah 3: Jumlah besar: serahkan ke pengelola limbah."
        ),
    },
    "Asam Stearat": {
        "rumus": "C₁₈H₃₆O₂ (asam oktadekanoat)",
        "simbol_bahaya": "Iritasi",
        # GHS: GHS07 (iritasi ringan)
        "wujud": "Padatan lilin putih",
        "bau": "Tidak berbau atau bau lilin lemah",
        "reaktivitas": (
            "Sangat stabil; "
            "asam lemak jenuh (tidak ada ikatan rangkap); "
            "bereaksi dengan basa membentuk sabun (stearat logam/alkali); "
            "tidak reaktif dengan air; tidak mudah terbakar pada suhu kamar; "
            "titik leleh 69–72°C"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan padatan dalam wadah tertutup.\n"
            "Langkah 2: Buang ke tempat sampah umum jika bersih."
        ),
    },
    "Parafin Padat": {
        "rumus": "CₙH₂ₙ₊₂ (n = 20–40; campuran alkana rantai panjang)",
        # KOREKSI: rumus C₂₅H₅₂ tidak tepat — parafin adalah campuran
        "simbol_bahaya": "Tidak Berbahaya",
        # GHS: tidak ada piktogram
        "wujud": "Padatan putih atau transparan (lilin)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Sangat stabil; inert terhadap asam, basa, dan oksidator encer; "
            "tidak reaktif secara kimia pada suhu kamar; "
            "dapat terbakar pada suhu tinggi (titik nyala >100°C); "
            "campuran alkana jenuh rantai panjang; "
            "titik leleh bervariasi 47–65°C sesuai grade"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan padatan dalam wadah tertutup.\n"
            "Langkah 2: Buang ke tempat sampah umum jika bersih. "
            "Jangan dalam jumlah besar ke saluran (dapat memblok)."
        ),
    },

    # ── GARAM SENG & BESI ─────────────────────────────────────────────
    "Seng Sulfat": {
        "rumus": "ZnSO₄",
        "simbol_bahaya": "Beracun | Iritasi | Bahaya Lingkungan",
        # GHS: GHS06 (toksik), GHS07 (iritasi), GHS09 (bahaya lingkungan)
        "wujud": "Padatan kristal putih (heptahidrat: ZnSO₄·7H₂O, vitriol putih)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; higroskopis; "
            "larut dalam air; "
            "bereaksi dengan basa membentuk endapan Zn(OH)₂ putih yang amfoter "
            "(larut dalam basa berlebih → [Zn(OH)₄]²⁻); "
            "toksik: LD₅₀ tikus oral = 2.200 mg/kg (ZnSO₄); "
            "sangat toksik bagi organisme akuatik (bioakumulatif)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Kumpulkan dalam wadah plastik berlabel 'LIMBAH LOGAM BERAT – Zn'.\n"
            "Langkah 2: JANGAN campur dengan limbah organik.\n"
            "Langkah 3: Endapkan Zn²⁺ dengan NaOH → Zn(OH)₂; saring.\n"
            "Langkah 4: Serahkan ke pengelola limbah B3 — Zn bioakumulatif di akuatik."
        ),
    },
    "Besi(II) Sulfat": {
        "rumus": "FeSO₄",
        "simbol_bahaya": "Iritasi | Bahaya Lingkungan",
        # GHS: GHS07 (iritasi), GHS09 (bahaya lingkungan)
        # KOREKSI: "Iritasi" sudah benar, tambahkan bahaya lingkungan
        "wujud": "Padatan kristal hijau biru (heptahidrat, vitriol hijau); "
                 "putih jika teroksidasi (besi(III) sulfat)",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil dalam bentuk heptahidrat; "
            "teroksidasi oleh udara dan oksidator menjadi Fe(III) sulfat (coklat); "
            "bereaksi dengan basa membentuk endapan Fe(OH)₂ hijau pucat "
            "yang teroksidasi cepat menjadi Fe(OH)₃ coklat; "
            "agen pereduksi ringan; "
            "toksik bagi organisme akuatik"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Netralisasi pH hingga 6–8 (terbentuk endapan Fe(OH)₂/Fe(OH)₃).\n"
            "Langkah 3: Saring endapan; buang ke limbah padat B3.\n"
            "Langkah 4: Filtrat dapat dibuang ke saluran pembuangan."
        ),
    },

    # ── BIOMOLEKUL / BIOMARKER ────────────────────────────────────────
    "Kreatinin": {
        "rumus": "C₄H₇N₃O",
        "simbol_bahaya": "Tidak Berbahaya (non-hazardous)",
        # GHS: tidak ada piktogram
        "wujud": "Padatan kristal putih",
        "bau": "Tidak berbau",
        "reaktivitas": (
            "Stabil pada suhu kamar; "
            "larut dalam air; "
            "tidak reaktif dalam kondisi normal; "
            "produk metabolisme kreatin di otot; "
            "biomarker fungsi ginjal (GFR); "
            "bereaksi dengan pikrat basa membentuk warna merah-jingga "
            "(reaksi Jaffé, metode pengukuran klinis)"
        ),
        "pengelolaan_limbah": (
            "Langkah 1: Encerkan dengan air minimal 1:10.\n"
            "Langkah 2: Buang ke saluran pembuangan dengan air mengalir."
        ),
    },
}
