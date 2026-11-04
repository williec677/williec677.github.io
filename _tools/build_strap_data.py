import json, re
WB="https://watchbase.com/"
M=[]
def add(brand, model, refs, case, lug, stock, styles, notes, sources, fit="standard", slug=None, q=None):
    s = slug or re.sub(r'[^a-z0-9]+','-',(brand+' '+model).lower()).strip('-')
    M.append(dict(id=s, brand=brand, model=model, refs=refs, case=case, lug=lug, fit=fit,
                  stock=stock, styles=styles, notes=notes, sources=sources, q=q))

R="Rolex"
OY="Oyster bracelet"
add(R,"Submariner 41",["124060","126610LN","126610LV"],"41mm",21,OY,["Rubber (curved end)","FKM rubber","NATO","Leather"],
 "The 2020 Submariner moved to 21mm, so your old 20mm Sub straps will not fit. Rolex lug holes sit close to the case, so curved spring bars or curved end rubber give the cleanest look.",
 [WB+"rolex/x/126610ln",WB+"rolex/x/124060","https://www.modacommunities.com/glossary/guides/rolex-bracelets"],slug="rolex-submariner-41")
add(R,"Submariner 40 (2010 to 2020)",["114060","116610LN","116610LV"],"40mm",20,OY,["Rubber (curved end)","NATO","Leather","Oyster style bracelet"],
 "The Maxi case Submariner is a true 20mm, the easiest Sub to shop straps for. Same 20mm as the Sub before it, but different from the 21mm Sub that replaced it.",
 [WB+"rolex/x/116610ln",WB+"rolex/x/114060"],slug="rolex-submariner-40")
add(R,"Submariner Date 16610",["16610"],"40mm",20,OY,["NATO","Rubber","Leather","Oyster style bracelet"],
 "The classic five digit Sub. 20mm between the lugs with drilled lug holes on most cases, which makes strap swaps easy.",
 [WB+"rolex/submariner/16610-comex","https://www.modacommunities.com/glossary/guides/rolex-bracelets"],slug="rolex-submariner-16610")
add(R,"GMT-Master II (current 126710)",["126710BLRO","126710BLNR","126710GRNR","126720VTNR"],"40mm",20,"Oyster or Jubilee bracelet",["Jubilee style bracelet","Rubber (curved end)","NATO","Leather"],
 "Every steel GMT-Master II in the 40mm case is 20mm. Rolex sells it on Oyster and Jubilee, and the Jubilee look is the one people chase.",
 [WB+"rolex/gmt-master/126710blro-0001","https://www.modacommunities.com/glossary/guides/rolex-bracelets"],slug="rolex-gmt-master-ii-126710")
add(R,"GMT-Master II 116710",["116710LN","116710BLNR"],"40mm",20,OY,["Rubber (curved end)","NATO","Jubilee style bracelet","Leather"],
 "The ceramic Maxi case GMT. Still 20mm, so anything that fits the current GMT fits here too.",
 [WB+"rolex/x/116710ln"],slug="rolex-gmt-master-ii-116710")
add(R,"GMT-Master II 16710",["16710"],"40mm",20,"Oyster or Jubilee bracelet",["Jubilee style bracelet","NATO","Leather","Rubber"],
 "The aluminum bezel GMT people love. 20mm lugs with drilled holes on most examples, which makes it a fantastic NATO watch.",
 [WB+"rolex/x/16710"],slug="rolex-gmt-master-ii-16710")
add(R,"Datejust 36",["126200","126234","116234"],"36mm",20,"Jubilee or Oyster bracelet",["Jubilee style bracelet","Leather","Suede","Oyster style bracelet"],
 "The 36mm Datejust has been 20mm for generations. A dressy leather or suede strap looks great on it.",
 [WB+"rolex/datejust/126200-0001",WB+"rolex/datejust/126234-0011",WB+"rolex/datejust/116234-0078"],slug="rolex-datejust-36")
add(R,"Datejust 41",["126300","126334"],"41mm",21,"Jubilee or Oyster bracelet",["Leather","Rubber (curved end)","Suede","Jubilee style bracelet"],
 "The 41mm Datejust is 21mm, not 20mm. Plenty of cheap straps only come in 20mm or 22mm, so check the size before you buy.",
 [WB+"rolex/datejust-41/126300-0001",WB+"rolex/datejust-41/126334-0001","https://www.modacommunities.com/glossary/guides/rolex-bracelets"],slug="rolex-datejust-41")
add(R,"Sea-Dweller 43",["126600"],"43mm",22,OY,["Rubber (curved end)","FKM rubber","NATO","Sailcloth"],
 "The 43mm Sea-Dweller jumped to 22mm. The older 40mm Sea-Dweller 116600 was 20mm, so do not mix them up.",
 ["https://tempuseuropa.com/en/reference/rolex-sea-dweller-126600","https://www.modacommunities.com/glossary/guides/rolex-bracelets","https://www.bobswatches.com/pre-owned-red-writing-rolex-sea-dweller-ref-126600-black-dial.html"],slug="rolex-sea-dweller-126600")
add(R,"Deepsea 44",["136660"],"44mm",21,OY,["Rubber (curved end)","FKM rubber","NATO"],
 "A huge watch with 21mm lugs. Thick rubber suits its tool watch vibe best.",
 [WB+"rolex/sea-dweller/136660-0003"],slug="rolex-deepsea-136660")
add(R,"Yacht-Master 40 (steel)",["126622"],"40mm",20,OY,["Rubber (curved end)","Leather","NATO","Sailcloth"],
 "The Rolesium Yacht-Master 40 is a straight 20mm. Note that gold Yacht-Masters on Oysterflex use a fitted strap, not standard spring bars.",
 [WB+"rolex/yacht-master/126622-0001"],slug="rolex-yacht-master-40")
add(R,"Yacht-Master 42",["226659"],"42mm",21,"Oysterflex",["Rubber (curved end)","FKM rubber","Sailcloth"],
 "Comes on Rolex's Oysterflex, a rubber covered metal blade. Aftermarket 21mm curved end rubber is the closest swap.",
 ["https://helvetus.com/blogs/rolex-strap-guide/rolex-yacht-master-42-226659-rubber-strap-guide","https://delugs.com/pages/rolex-yacht-master-42-226659-0004"],slug="rolex-yacht-master-42")
add(R,"Explorer 36 (2021)",["124270"],"36mm",19,OY,["Leather","Suede","NATO","Canvas"],
 "Heads up: the current 36mm Explorer is 19mm. The older 114270 and 14270 were 20mm, so check your reference.",
 ["https://wornandwound.com/review/rolex-looks-the-new-explorer-124270-review/","https://www.fratellowatches.com/strap-width-an-oft-forgotten-spec-that-makes-a-world-of-difference/","https://www.twostitchstraps.com/en-us/blogs/strap-guides/rolex-explorer-1-strap-guide"],slug="rolex-explorer-36")
add(R,"Explorer 40",["224270"],"40mm",21,OY,["Leather","Suede","NATO","Canvas"],
 "The 40mm Explorer uses 21mm lugs, so straps from the 39mm Explorer will not fit.",
 ["https://tempuseuropa.com/en/reference/rolex-explorer-40-224270","https://www.twostitchstraps.com/en-us/blogs/strap-guides/rolex-explorer-1-strap-guide"],slug="rolex-explorer-40")
add(R,"Explorer 39",["214270"],"39mm",20,OY,["Leather","NATO","Suede","Canvas"],
 "The 39mm Explorer is 20mm, which opens up a huge world of straps.",
 [WB+"rolex/explorer/214270-0001","https://www.twostitchstraps.com/en-us/blogs/strap-guides/rolex-explorer-1-strap-guide"],slug="rolex-explorer-39")
add(R,"Explorer II 216570",["216570"],"42mm",21,OY,["Leather","Rubber (curved end)","NATO","Canvas"],
 "The 216570 is 21mm. Sources disagree on the newer 226570, so we left that one out until we can confirm it.",
 [WB+"rolex/explorer-2/216570-0001","https://cnswatchbands.com/blog/best-straps-for-the-rolex-explorer-i-ii/"],slug="rolex-explorer-ii-216570")
add(R,"Oyster Perpetual 41",["124300"],"41mm",21,OY,["Leather","Rubber (curved end)","NATO","Suede"],
 "The OP 41 shares the 21mm width of the Datejust 41 and Submariner 41.",
 [WB+"rolex/oyster-perpetual/124300-0001"],slug="rolex-oyster-perpetual-41")
add(R,"Oyster Perpetual 36",["126000"],"36mm",20,OY,["Leather","Suede","NATO","Rubber"],
 "A 20mm OP 36 on a colorful NATO or a suede strap is a fun summer look.",
 [WB+"rolex/oyster-perpetual-36/126000-0001"],slug="rolex-oyster-perpetual-36")
add(R,"Cosmograph Daytona (steel)",["126500LN","116500LN"],"40mm",20,OY,["Rubber (curved end)","Leather","Oyster style bracelet"],
 "Both recent steel Daytonas are 20mm. Leather racing straps look sharp on them.",
 [WB+"rolex/daytona/126500ln-0001",WB+"rolex/daytona/116500ln-0001","https://www.modacommunities.com/glossary/guides/rolex-bracelets"],slug="rolex-daytona")
add(R,"Air-King 116900",["116900"],"40mm",20,OY,["NATO","Leather","Rubber"],
 "This is the 116900. We have not confirmed the newer 126900 yet, so it is not listed.",
 [WB+"rolex/x/116900"],slug="rolex-air-king-116900")

O="Omega"
add(O,"Speedmaster Professional Moonwatch",["310.30.42.50.01.001","310.30.42.50.01.002","311.30.42.30.01.005"],"42mm",20,"Steel bracelet",["NATO","Leather","Velcro","Rubber"],
 "The Moonwatch is 20mm and one of the best strap swap watches ever made. Older 3570.50 and 311 references are also 20mm.",
 [WB+"omega/x/310-30-42-50-01-001",WB+"omega/x/311-30-42-30-01-005"],slug="omega-speedmaster-professional")
add(O,"Seamaster Diver 300M (42mm)",["210.30.42.20.01.001","210.30.42.20.03.001"],"42mm",20,"Steel bracelet or rubber strap",["Rubber","NATO","Leather","Mesh"],
 "The current Seamaster 300M is 20mm. The lugs are fairly long and curved, so curved end rubber hugs it nicely.",
 [WB+"omega/x/210-30-42-20-01-001",WB+"omega/x/210-30-42-20-03-001"],slug="omega-seamaster-300m")
add(O,"Seamaster 300M 2531.80 (41mm)",["2531.80"],"41mm",20,"Steel bracelet",["Rubber","NATO","Leather"],
 "The Bond era wave dial Seamaster is 20mm, same as the current one.",
 ["https://www.omegawatches.com/en-us/watch-omega-seamaster-300-m-chronometer-25318000","https://www.bernardwatch.com/Omega/Seamaster-Professional/OMG4521"],slug="omega-seamaster-300m-2531-80")
add(O,"Seamaster Aqua Terra 41mm",["220.10.41.21.01.001","220.10.41.21.03.001"],"41mm",20,"Steel bracelet, leather or rubber strap",["Leather","Rubber","NATO"],
 "Omega lists 20mm between the lugs on the 41mm Aqua Terra.",
 [WB+"omega/x/220-10-41-21-01-001","https://www.omegawatches.com/media/pdf/watches/product-sheet/us/en-us/22010412103004-en-us.pdf"],slug="omega-aqua-terra-41")
add(O,"Seamaster Aqua Terra 38mm",["220.10.38.20.01.001","220.10.38.20.10.001"],"38mm",19,"Steel bracelet or leather strap",["Leather","Suede","Rubber"],
 "The 38mm Aqua Terra is 19mm, a size that is harder to find than 20mm.",
 [WB+"omega/x/220-10-38-20-01-001","https://www.omegawatches.com/media/pdf/watches/product-sheet/us/en-us/22010382010001-en-us.pdf"],slug="omega-aqua-terra-38")
add(O,"Seamaster Planet Ocean 43.5mm",["215.30.44.21.01.001"],"43.5mm",21,"Steel bracelet or rubber strap",["Rubber","NATO","Sailcloth"],
 "The 43.5mm Planet Ocean is 21mm.",
 [WB+"omega/x/215-30-44-21-01-001"],slug="omega-planet-ocean-43-5")
add(O,"Seamaster 300 (41mm)",["234.30.41.21.01.001"],"41mm",21,"Steel bracelet",["Leather","NATO","Rubber"],
 "The heritage style Seamaster 300 uses 21mm lugs.",
 [WB+"omega/x/234-30-41-21-01-001"],slug="omega-seamaster-300-heritage")
add("Omega x Swatch","MoonSwatch",["SO33M100 and all Mission models"],"42mm",20,"Velcro strap",["Velcro","NATO","Rubber"],
 "20mm, but the bioceramic lugs are short and the case is light, so thin NATO or Velcro straps work better than thick leather. Use quick release spring bars to avoid scratching the lugs.",
 [WB+"swatch/x/so33m100"],slug="omega-swatch-moonswatch")

T="Tudor"
add(T,"Black Bay 58",["M79030N","M79030B"],"39mm",20,"Steel bracelet, leather or fabric strap",["Fabric","NATO","Leather","Rubber"],
 "The BB58 is 20mm, which makes it one of the easiest luxury divers to strap up. Tudor's own fabric straps are a fan favorite.",
 [WB+"tudor/x/m79030n-0001"],slug="tudor-black-bay-58")
add(T,"Black Bay 41 (M79230)",["M79230N","M79230R","M79230B"],"41mm",22,"Steel bracelet, leather or fabric strap",["Fabric","Leather","NATO","Rubber"],
 "The classic Black Bay 41 is 22mm. Thick distressed leather looks great on this chunky case.",
 ["https://dialsize.com/tudor/black-bay/79230n/",WB+"tudor/black-bay/79230n-0008"],slug="tudor-black-bay-41")
add(T,"Black Bay 41 (2023 Master Chronometer)",["M7941A1A0RU"],"41mm",22,"Steel bracelet or rubber strap",["Rubber","Fabric","Leather","NATO"],
 "The updated Black Bay with the MT5602-U movement is still 22mm.",
 [WB+"tudor/x/m7941a1a0ru-0001"],slug="tudor-black-bay-41-master-chronometer")
add(T,"Black Bay 54",["M79000N"],"37mm",20,"Steel bracelet or rubber strap",["Rubber","Fabric","NATO","Leather"],
 "The small BB54 is 20mm, same as the BB58.",
 ["https://www.tudorwatch.com/en/watches/black-bay-54/m79000n-0001","https://tempuseuropa.com/en/reference/tudor-black-bay-54-m79000n-0001"],slug="tudor-black-bay-54")
add(T,"Black Bay 36",["M79500"],"36mm",19,"Steel bracelet, leather or fabric strap",["Leather","Fabric","NATO"],
 "The BB36 is 19mm, so 20mm straps will not sit right.",
 [WB+"tudor/black-bay-one/79500-0013"],slug="tudor-black-bay-36")
add(T,"Black Bay GMT",["M79830RB"],"41mm",22,"Steel bracelet, leather or fabric strap",["Fabric","Leather","NATO","Rubber"],
 "The Pepsi Black Bay GMT is 22mm.",
 [WB+"tudor/x/m79830rb-0001"],slug="tudor-black-bay-gmt")
add(T,"Black Bay Pro",["M79470"],"39mm",22,"Steel bracelet, fabric or rubber strap",["Fabric","Rubber","NATO"],
 "Small 39mm case, big 22mm lugs. It gives the Pro its chunky tool watch look.",
 [WB+"tudor/x/m79470-0001"],slug="tudor-black-bay-pro")
add(T,"Pelagos 42",["M25600TN","M25600TB"],"42mm",22,"Titanium bracelet plus rubber strap",["Rubber","Fabric","NATO"],
 "The Pelagos 42 is 22mm and ships with both a titanium bracelet and a rubber strap. The Pelagos FXD has fixed bars and needs a one piece pass through strap instead.",
 [WB+"tudor/x/m25600tn-0001"],slug="tudor-pelagos-42")
add(T,"Pelagos 39",["M25407N"],"39mm",21,"Titanium bracelet plus rubber strap",["Rubber","Fabric","NATO"],
 "The Pelagos 39 is 21mm, not 20mm or 22mm like its siblings.",
 ["https://www.tudorwatch.com/en/watches/pelagos/m25407n-0001","https://jamieson-carry.com/tudor-pelagos-39-25407n-0001"],slug="tudor-pelagos-39")
add(T,"Ranger",["M79950"],"39mm",20,"Steel bracelet, fabric, leather or rubber strap",["Fabric","NATO","Canvas","Leather"],
 "The Ranger is 20mm and made for field straps.",
 [WB+"tudor/x/m79950-0001"],slug="tudor-ranger")

add("Grand Seiko","SBGM221 GMT",["SBGM221"],"39.5mm",19,"Leather strap",["Leather","Suede","Alligator style leather"],
 "The cream dial GS GMT is 19mm. It is a dress watch at heart, so stick with slim leather.",
 ["https://tempuseuropa.com/en/reference/grand-seiko-elegance-gmt-sbgm221","https://www.theseikoguy.com/watches/sbgm221","https://grandseikoboutique.us/products/watch-automatic-gmt-strap-sbgm221"],slug="grand-seiko-sbgm221")

S="Seiko"
add(S,"SKX007 / SKX009",["SKX007","SKX009"],"42mm",22,"Rubber strap or steel bracelet",["Rubber","NATO","Jubilee style bracelet","FKM rubber"],
 "The legendary SKX is 22mm. Aftermarket bracelets and straps for it are everywhere.",
 [WB+"seiko/mechanical/skx007k1"],slug="seiko-skx007")
add(S,"SKX013",["SKX013"],None,20,"Rubber strap or steel bracelet",["Rubber","NATO","Jubilee style bracelet"],
 "The midsize SKX is 20mm, so it does not share straps with the 22mm SKX007.",
 ["https://strapsco.com/seiko-skx013-lug-width-strap-size/","https://www.watchsleuth.com/seikodiverfinder/search/?MOD=SKX013"],slug="seiko-skx013")
add(S,"Prospex SPB143 (62MAS reissue)",["SPB143","SPB149"],"40.5mm",20,"Steel bracelet",["Rubber","NATO","Leather","Fabric"],
 "The SPB143 is 20mm, which makes it easy to dress up or down.",
 ["https://www.seikowatches.com/no-en/products/prospex/spb143j1","https://tempuseuropa.com/en/reference/seiko-prospex-1965-divers-spb143j1","https://strapsco.com/seiko-prospex-spb143-62mas-lug-width-strap-size/"],slug="seiko-spb143")
add(S,"5 Sports (SRPD)",["SRPD55","SRPD51","SRPD63"],"42.5mm",22,"Steel bracelet or silicone strap",["NATO","Rubber","Jubilee style bracelet","Canvas"],
 "Seiko lists 22mm between the lugs on the SRPD 5 Sports. This is the modding king, and it takes the same 22mm straps as the SKX.",
 ["https://www.seikowatches.com/us-en/products/5sports/srpd55"],slug="seiko-5-sports-srpd")
add(S,"Presage Cocktail Time SRPB43",["SRPB43"],"40.5mm",20,"Steel bracelet",["Leather","Suede","Mesh"],
 "Seiko lists 20mm between the lugs. A blue or brown leather strap turns this into a killer dress watch.",
 ["https://www.seikowatches.com/us-en/products/presage/srpb43j1","https://www.seikowatch.us/presage/presage-cocktail-time-srpb43/"],slug="seiko-presage-srpb43")
add(S,"Prospex Alpinist SPB121",["SPB121"],"39.5mm",20,"Leather strap or steel bracelet",["Leather","NATO","Canvas"],
 "Seiko lists 20mm between the lugs on the Alpinist.",
 ["https://www.seikowatches.com/uk-en/products/prospex/spb121j1","https://www.theseikoguy.com/watches/spb121"],slug="seiko-alpinist-spb121")
add(S,"Prospex Turtle",["SRPE93","SRP777"],"45mm",22,"Silicone strap or steel bracelet",["Rubber","NATO","FKM rubber"],
 "The Turtle is 22mm. Seiko lists it on the official page.",
 ["https://www.seikowatches.com/us-en/products/prospex/srpe93",WB+"seiko/x/srp777"],slug="seiko-turtle")
add(S,"Seiko 5 SNK809",["SNK809","SNK807","SNK805"],"37mm",18,"Canvas strap",["NATO","Canvas","Leather"],
 "The little SNK is 18mm. A cheap watch that looks great on a two piece leather or a NATO.",
 ["https://strapsco.com/seiko-5-skn805-snk807-snk809-lug-width-strap-size/","https://www.watchsleuth.com/seiko5finder/search/?MOD=SNK809"],slug="seiko-5-snk809")

C="Citizen"
add(C,"Promaster Diver BN0150",["BN0150-28E","BN0150"],"44mm",20,"Rubber strap",["Rubber","NATO","Canvas"],
 "Citizen lists a 20mm lug width on the official product page.",
 ["https://www.citizenwatch.com/us/en/product/BN0150-28E.html"],slug="citizen-promaster-bn0150")
add(C,"Promaster Fugu NY0040",["NY0040-09E","NY0040"],None,20,"Rubber strap",["Rubber","NATO","Jubilee style bracelet"],
 "The Fugu takes 20mm, and Citizen's own replacement bracelet for it is 20mm.",
 ["https://rolliponiz.it/en/products/bracciale-59-r00684-20mm-per-citizen-promaster-ny0040-ny0084-ny0085-ny0086-fugu","https://timevibe.fi/product/citizen-ny0040-09e-promaster-fugu/"],slug="citizen-promaster-fugu")
add(C,"Tsuyosa",["NJ0150"],"40mm",None,"Integrated bracelet",["Integrated bracelet only"],
 "The Tsuyosa uses an integrated bracelet. Citizen lists the lug width as just 9.1mm, so normal straps do not fit without a model specific adapter.",
 ["https://www.citizenwatch.com/us/en/product/NJ0150-56W.html"],fit="integrated",slug="citizen-tsuyosa")

H="Hamilton"
add(H,"Khaki Field Mechanical 38",["H69439931","H69439"],"38mm",20,"Fabric (NATO style) or leather strap",["NATO","Canvas","Leather"],
 "Hamilton's field watch is 20mm and lives on NATO straps.",
 [WB+"hamilton/x/h69439931"],slug="hamilton-khaki-field-mechanical")
add(H,"Khaki Field Auto 38",["H70455533","H70455"],"38mm",20,"Steel bracelet, leather or fabric strap",["NATO","Leather","Canvas"],
 "The 38mm Khaki Field Auto is 20mm.",
 [WB+"hamilton/x/h70455533"],slug="hamilton-khaki-field-auto-38")
add(H,"Khaki Field Auto 42",["H70555533","H70555"],"42mm",22,"Steel bracelet, leather or fabric strap",["NATO","Leather","Canvas"],
 "The 42mm Khaki Field Auto steps up to 22mm.",
 [WB+"hamilton/x/h70555533"],slug="hamilton-khaki-field-auto-42")

TI="Tissot"
add(TI,"PRX Powermatic 80 (40mm)",["T137.407"],"40mm",None,"Integrated bracelet",["PRX specific rubber","PRX specific leather"],
 "Integrated bracelet with a 12mm attachment. Regular straps do not fit. Buy straps made for the PRX and your case size.",
 [WB+"tissot/x/t137-407-11-041-00"],fit="integrated",slug="tissot-prx-powermatic-80",q="tissot+prx+40mm+strap")
add(TI,"PRX Quartz (40mm)",["T137.410"],"40mm",None,"Integrated bracelet",["PRX specific rubber","PRX specific leather"],
 "Same 12mm integrated attachment as the automatic. Look for PRX specific straps.",
 [WB+"tissot/x/t137-410-11-041-00"],fit="integrated",slug="tissot-prx-quartz",q="tissot+prx+40mm+strap")
add(TI,"Gentleman Powermatic 80",["T127.407"],"40mm",21,"Steel bracelet or leather strap",["Leather","Rubber","NATO"],
 "The Gentleman is 21mm.",
 [WB+"tissot/x/t127-407-11-041-00"],slug="tissot-gentleman")

add("TAG Heuer","Carrera Chronograph 39mm",["CBS2210"],"39mm",20,"Leather strap or steel bracelet",["Leather","Rally leather","Rubber"],
 "TAG lists the original strap at 20mm where it meets the case.",
 ["https://www.tagheuer.com/int/en/timepieces/collections/tag-heuer-carrera/39-mm-th20-00/CBS2210.BA0048.html","https://tempuseuropa.com/en/reference/tag-heuer-carrera-chronograph-39-cbs2210-fc6534"],slug="tag-heuer-carrera-39")
add("TAG Heuer","Aquaracer Professional 300 (43mm)",["WBP201A"],"43mm",21,"Steel bracelet or rubber strap",["Rubber","NATO"],
 "21mm. The factory rubber strap is fitted to the case, so for aftermarket straps order 21mm.",
 ["https://delugs.com/pages/straps-for-tag-heuer-aquaracer-watches"],slug="tag-heuer-aquaracer-300")

add("Christopher Ward","C60 Trident Pro 300 (40mm)",["C60-40ADA31S0KK1"],"40mm",20,"Steel bracelet or rubber strap",["Rubber","NATO","Sailcloth"],
 "Christopher Ward lists 20mm for the 40mm case.",
 ["https://www.christopherward.com/trident-pro-300-watches/c60-trident-pro-300/C60-40ADA31S0KK1-B0.html"],slug="christopher-ward-c60-trident-pro-300")
add("Mido","Multifort Automatic",["M005.430"],"42mm",22,"Steel bracelet",["Leather","NATO","Rubber"],
 "The 42mm Multifort is 22mm.",
 [WB+"mido/x/m005-430-11-031-80"],slug="mido-multifort")
add("Bulova","Precisionist Champlain",["96B131"],None,24,"Steel bracelet",["Rubber","Leather"],
 "A big 24mm, so look for wide rubber or leather straps.",
 ["https://wristsushi.proboards.com/thread/13558/bulova-precisionist-champlain-96b131","https://www.bablas.co.uk/bulova-precisionist-gents-watch-96b131.html"],slug="bulova-precisionist-96b131")

CA="Casio"
add(CA,"G-Shock DW-5600",["DW-5600E"],None,None,"Resin strap",["G-Shock adapter plus NATO","G-Shock adapter plus rubber"],
 "Proprietary 16mm resin mount. Use a DW-5600 adapter kit, then a 22mm or 24mm strap.",
 ["https://www.strapify.com.au/products/g-shock-16mm-to-22mm-adapter","https://www.strapmod.com/guides/watch-lug-width-chart/"],fit="proprietary",slug="casio-g-shock-dw-5600",q="dw5600+strap+adapter")
add(CA,"G-Shock GA-2100 (CasiOak)",["GA-2100","GA-B2100"],"45.4mm",None,"Resin strap",["G-Shock adapter plus NATO","G-Shock adapter plus rubber"],
 "Proprietary mount with 16mm spring bar holes. Casio and others sell adapters that let you use 20mm or 22mm straps.",
 ["https://www.g-central.com/how-to-get-official-strap-adapters-for-g-shock-dw-5600-ga-2100-ga-b2100-gm-2100/","https://watchstrapsize.com/casio-g-shock-ga-2100-casioak-strap-size/"],fit="proprietary",slug="casio-g-shock-ga-2100",q="ga2100+strap+adapter")
add(CA,"Duro MDV106",["MDV106","MDV-106"],"44mm",22,"Resin strap",["NATO","Rubber","Jubilee style bracelet"],
 "The Duro is 22mm and might be the best value strap monster on this list.",
 ["https://watchthedetails.com/watches/casio/mdv-106","https://12and60.com/casio-duro-mdv-106-watch-review/"],slug="casio-duro-mdv106")

add("Orient","Bambino 38 (Version 7)",["RA-AC0M"],"38.4mm",20,"Leather strap or steel bracelet",["Leather","Suede","Mesh"],
 "Orient lists 20mm for the 38.4mm Bambino. The bigger 40.5mm Bambino versions use a different width, so check your case size.",
 ["https://www.orientwatchusa.com/products/ra-ac0m04y30b","https://www.orientwatchusa.com/products/ra-ac0m03s30b"],slug="orient-bambino-38")
add("Orient","Kamasu",["RA-AA0004","RA-AA0001"],"41.8mm",22,"Steel bracelet",["Rubber","NATO","Leather"],
 "Orient lists 22mm for the Kamasu.",
 ["https://www.orientwatchusa.com/products/ra-aa0004e39b","https://www.orientwatch.co.uk/or/en_GB/c/orient-mako/p/RA-AA0004E"],slug="orient-kamasu")

L="Longines"
add(L,"HydroConquest 41mm",["L3.781"],"41mm",21,"Steel bracelet or rubber strap",["Rubber","NATO"],
 "The 41mm HydroConquest is 21mm.",
 [WB+"longines/x/l3-781-4-56-6"],slug="longines-hydroconquest-41")
add(L,"Spirit 40mm",["L3.810"],"40mm",21,"Steel bracelet or leather strap",["Leather","NATO","Canvas"],
 "The 40mm Spirit pilot watch is 21mm.",
 [WB+"longines/x/l3-810-4-73-6","https://watchstrapsize.com/longines-spirit-40-strap-size/"],slug="longines-spirit-40")
add("Breitling","Navitimer B01 Chronograph 43",["AB0138"],"43mm",22,"Steel bracelet or leather strap",["Leather","Alligator style leather"],
 "The 43mm Navitimer is 22mm. We have not confirmed the 41mm and 46mm sizes yet.",
 [WB+"breitling/x/ab0138211b1a1"],slug="breitling-navitimer-43")
add("Cartier","Santos de Cartier Medium",["WSSA0029"],"35mm",None,"Steel bracelet plus leather strap (QuickSwitch)",["Cartier QuickSwitch leather","Cartier QuickSwitch rubber"],
 "Uses Cartier's QuickSwitch system, about 18mm at the case. Regular spring bar straps do not fit, and Medium and Large QuickSwitch straps are not interchangeable.",
 ["https://ateliertaha.com/blogs/journal/cartier-santos-quickswitch-strap-guide"],fit="proprietary",slug="cartier-santos-medium",q="cartier+santos+quickswitch+strap")
add("Cartier","Tank Must Large",["WSTA0041"],"33.7 x 25.5mm",19,"Leather strap",["Leather","Suede","Alligator style leather"],
 "The Tank Must Large is 19mm. A slim leather strap keeps the dressy look.",
 ["https://www.cortinawatch.com/th/en/cartier/tank/wsta0041/","https://helvetus.com/blogs/cartier-strap-guide/cartier-tank-must-wsta0041-strap-guide"],slug="cartier-tank-must-large")
add("Panerai","Luminor 44mm",["PAM01312","PAM00510"],"44mm",24,"Leather strap",["Leather","Rubber","Canvas","Sailcloth"],
 "The 44mm Luminor is 24mm. Panerai straps use a tube and screw system on many cases, so check your lug hardware before buying.",
 [WB+"panerai/x/pam01312",WB+"panerai/x/pam00510"],slug="panerai-luminor-44")
add("IWC","Pilot's Watch Mark XX",["IW328201"],"40mm",20,"Leather strap or steel bracelet",["Leather","NATO","Canvas"],
 "The Mark XX is 20mm.",
 [WB+"iwc/x/iw328201"],slug="iwc-pilot-mark-xx")
add("IWC","Pilot's Watch Mark XVIII",["IW327001"],"40mm",20,"Leather strap",["Leather","NATO","Canvas"],
 "The Mark XVIII is 20mm, same as the Mark XX.",
 [WB+"iwc/x/iw327001"],slug="iwc-pilot-mark-xviii")
add("Oris","Divers Sixty-Five 40mm",["01 733 7707 4053"],"40mm",20,"Steel bracelet or leather strap",["Leather","NATO","Rubber"],
 "Oris lists 20mm on the 40mm Divers Sixty-Five.",
 ["https://www.oris.ch/en-US/product/watch/divers/divers-sixty-five/01-733-7707-4053-07-8-20-18"],slug="oris-divers-sixty-five-40")
add("Sinn","556",["556.010"],"38.5mm",20,"Steel bracelet or leather strap",["NATO","Leather","Canvas"],
 "The Sinn 556 is 20mm.",
 [WB+"sinn/x/556-010"],slug="sinn-556")


import os
def plus(t): return re.sub(r'[^a-z0-9]+','+',t.lower()).strip('+')
STYLEQ={"Rubber (curved end)":"curved end rubber watch strap","FKM rubber":"fkm rubber watch strap","NATO":"nato watch strap","Leather":"leather watch strap",
"Suede":"suede watch strap","Fabric":"fabric watch strap","Canvas":"canvas watch strap","Rubber":"rubber watch strap","Velcro":"velcro watch strap",
"Mesh":"mesh watch bracelet","Sailcloth":"sailcloth watch strap","Oyster style bracelet":"oyster style watch bracelet","Jubilee style bracelet":"jubilee style watch bracelet",
"Alligator style leather":"alligator grain leather watch strap","Rally leather":"rally leather watch strap"}
for m in M:
    name=f'{m["brand"]} {m["model"]}'
    refs=", ".join(m["refs"])
    case=f' and a {m["case"]} case' if m["case"] else ''
    if m["fit"]=="standard":
        m["line"]=f'The {name} ({refs}) has a {m["lug"]}mm lug width{case}, so it takes {m["lug"]}mm straps.'
        m["shop"]=[{"t":f'{m["lug"]}mm {STYLEQ[st].replace(" watch","")}',"q":plus(f'{m["lug"]}mm {STYLEQ[st]}')} for st in m["styles"][:3]]
    else:
        kind="an integrated bracelet" if m["fit"]=="integrated" else "a proprietary strap fitting"
        m["line"]=f'The {name} ({refs}) uses {kind}{case}, so standard spring bar straps do not fit without a model specific strap or adapter.'
        m["shop"]=[{"t":f'{m["model"].split(" (")[0]} compatible straps',"q":m["q"]}]
    m["ebay_q"]=plus(m["brand"].split(" x ")[-1]+" "+m["model"].split(" (")[0]+" strap")
    m.pop("q")
ids=[m["id"] for m in M]; assert len(ids)==len(set(ids))
M.sort(key=lambda m:(m["brand"],m["model"]))
B=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json.dump(M,open(B+"/_data/straps.json","w"),indent=1,ensure_ascii=False)
sizes=[]
for w in sorted({m["lug"] for m in M if m["fit"]=="standard"}):
    sizes.append({"mm":w,"ids":[m["id"] for m in M if m["lug"]==w and m["fit"]=="standard"]})
json.dump({"sizes":sizes,"special":[m["id"] for m in M if m["fit"]!="standard"]},open(B+"/_data/strap_sizes.json","w"),indent=1)
# stubs
d=B+"/strap-finder"; os.makedirs(d,exist_ok=True)
for f in os.listdir(d):
    if f!="index.html": os.remove(os.path.join(d,f))
for m in M:
    name=f'{m["brand"]} {m["model"]}'
    lugtxt=f'{m["lug"]}mm lug width' if m["fit"]=="standard" else ("integrated bracelet" if m["fit"]=="integrated" else "proprietary strap fit")
    title=f'{name} Strap Size: '+' '.join(w if w[0].isdigit() else w.capitalize() for w in lugtxt.split())
    desc=m["line"]+" Strap ideas and fit notes inside."
    open(f'{d}/{m["id"]}.html','w').write(f'---\nlayout: strap-model\nstrap_id: {m["id"]}\ntitle: "{title}"\ndescription: "{desc}"\npermalink: /strap-finder/{m["id"]}/\n---\n')
# sources file
L=["# Watch Strap Finder sources","","Generated by the strap data script. One block per model in `_data/straps.json`. Every lug width was checked against the sources listed.",""]
for m in M:
    L.append(f'## {m["brand"]} {m["model"]} ({", ".join(m["refs"])})')
    L.append(f'Lug width: {str(m["lug"])+"mm" if m["lug"] else m["fit"]}. Case: {m["case"] or "not listed"}.')
    L+= [f'* {u}' for u in m["sources"]]+[""]
open(B+"/STRAP-FINDER-SOURCES.md","w").write("\n".join(L))
for m in M:
    for f in ("notes","model","stock","line"):
        assert "—" not in m[f] and "–" not in m[f] and " - " not in m[f], (m["id"],f)
print(len(M),[ (x["mm"],len(x["ids"])) for x in sizes])
