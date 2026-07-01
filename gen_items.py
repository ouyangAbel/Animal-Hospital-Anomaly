import os

base = r"C:\Users\tulia\animal-hospital-anomaly-guides"
domain = "https://animalhospitalanomalyguides.com"

# Read nav and footer from existing pages
with open(os.path.join(base, "boss-guides.html"), "r", encoding="utf-8") as f:
    boss = f.read()
nav = boss[boss.find('  <nav class="navbar"'):boss.find("  </nav>") + 8]

with open(os.path.join(base, "article-boss-fight-guide.html"), "r", encoding="utf-8") as f:
    art = f.read()
footer = art[art.find('  <footer class="site-footer">'):art.find("</html>")]

def build_page(ev):
    head = f'''    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{ev["title"]}</title>
    <meta name="description" content="{ev["description"]}">
    <meta name="keywords" content="{ev["keywords"]}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{domain}/{ev["filename"]}">
    <meta property="og:title" content="{ev["title"]}">
    <meta property="og:description" content="{ev["og_description"]}">
    <meta property="og:type" content="article">
    <link rel="stylesheet" href="style.css">
    <link rel="icon" type="image/webp" href="/images/favicon.webp">
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-RESXT38T4M"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag("js", new Date());
      gtag("config", "G-RESXT38T4M");
    </script>'''

    import urllib.parse
    et = urllib.parse.quote(ev["title"])
    url = f"{domain}/{ev['filename']}"
    share = f'''        <!-- Share Bar -->
          <div class="share-bar">
            <span class="share-bar-label">Share this guide:</span>
            <a class="share-btn share-btn-x" href="https://x.com/intent/post?text={et}&url={url}" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>X</a>
            <a class="share-btn share-btn-facebook" href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>Facebook</a>
            <a class="share-btn share-btn-reddit" href="https://reddit.com/submit?url={url}&title={et}" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24"><path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0zm5.01 4.744c.688 0 1.25.561 1.25 1.249a1.25 1.25 0 0 1-2.498.056l-2.597-.547-.8 3.747c1.824.07 3.48.632 4.674 1.488.308-.309.73-.491 1.207-.491.968 0 1.754.786 1.754 1.754 0 .716-.435 1.333-1.01 1.614a3.111 3.111 0 0 1 .042.52c0 2.694-3.13 4.87-7.004 4.87-3.874 0-7.004-2.176-7.004-4.87 0-.183.015-.366.043-.534A1.748 1.748 0 0 1 4.028 12c0-.968.786-1.754 1.754-1.754.463 0 .898.196 1.207.49 1.207-.883 2.878-1.43 4.744-1.487l.885-4.182a.342.342 0 0 1 .14-.197.35.35 0 0 1 .238-.042l2.906.617a1.214 1.214 0 0 1 1.108-.701zM9.25 12C8.561 12 8 12.562 8 13.25c0 .687.561 1.248 1.25 1.248.687 0 1.248-.561 1.248-1.249 0-.688-.561-1.249-1.249-1.249zm5.5 0c-.687 0-1.248.561-1.248 1.25 0 .687.561 1.248 1.249 1.248.688 0 1.249-.561 1.249-1.249 0-.687-.562-1.249-1.25-1.249zm-5.466 3.99a.327.327 0 0 0-.231.094.33.33 0 0 0 0 .463c.842.842 2.484.913 2.961.913.477 0 2.105-.056 2.961-.913a.361.361 0 0 0 .029-.463.33.33 0 0 0-.464 0c-.547.533-1.684.73-2.512.73-.828 0-1.979-.196-2.512-.73a.326.326 0 0 0-.232-.095z"/></svg>Reddit</a>
            <button class="share-btn share-btn-copy" data-url="{url}"><svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg><span class="share-btn-text">Copy Link</span></button>
          </div>'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
{head}
</head>
<body>
{nav}

  <main class="main-content">
    <div class="container">
      <div class="ad-placeholder ad-placeholder-top" aria-label="Advertisement"></div>
    </div>

    <header class="page-header page-header-article">
      <div class="container">
        <div class="breadcrumb">
          {ev["breadcrumb"]}
        </div>
        <h1>{ev["title"]}</h1>
        <p class="subtitle">{ev["og_description"]}</p>
      </div>
    </header>

    <div class="container">
      <article class="guide-article">
        <header class="guide-article-header">
          <span class="guide-article-tag">{ev["tag"]}</span>
          <div class="guide-article-meta">
            <time datetime="{ev["date"]}">{ev["date"]}</time>
            <span class="guide-article-sep">|</span>
            <span>{ev["read"]}</span>
          </div>
        </header>
        <div class="guide-article-body">
          {ev["content"]}

          <div class="inner-links">
            <h4>Related Guides</h4>
            <ul>
              <li><a href="equipment-guides.html">Items &amp; Shop Upgrades \u2014 Complete Reference</a></li>
              <li><a href="character-guides.html">Anomaly &amp; Enemy Guide \u2014 All Entities</a></li>
              <li><a href="article-how-to-survive.html">How to Survive \u2014 14 Reflex Tips</a></li>
              <li><a href="all-articles.html">All Articles \u2014 Browse All Guides</a></li>
            </ul>
          </div>
        </div>
{share}
      </article>

      <div class="ad-placeholder ad-placeholder-bottom" aria-label="Advertisement"></div>
    </div>
  </main>
{footer}
</body>
</html>'''

    filepath = os.path.join(base, ev["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath

# ===== 4 DETAIL PAGES =====
pages = [
    {
        "filename": "items-treatment.html",
        "title": "Animal Hospital Anomaly Treatment Items Guide: All 10 Free Spawn Items & Condition Map",
        "description": "Complete treatment items guide for Animal Hospital Anomaly. All 10 free spawn items, condition-to-item mappings, dual-use items, and the crucial Dehydration warning.",
        "keywords": "Animal Hospital Anomaly treatment items, condition item map, Bandages, IV Bag, Maple Syrup, Eye Drops, Cough Syrup, free spawn items",
        "og_description": "Every treatment item and what condition it cures \u2014 master the 10-item condition map in 10 minutes.",
        "tag": "Items Guide",
        "date": "2026-07-01",
        "read": "9 min read",
        "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="equipment-guides.html">Equipment Guides</a><span>/</span><span class="current">Treatment Items</span>',
        "content": '''<p>Treatment items are the backbone of every shift in Animal Hospital (Anomaly). There are exactly <strong>10 treatment items</strong>, all spawning for free outside their relevant treatment rooms. No shop purchase is needed. This guide covers every item, what condition it treats, dual-use functionality, and the one mistake that can be fatal.</p>

          <h3>The Condition \u2014 Item Map</h3>
          <p>Every patient condition has exactly one correct treatment item. Memorize this table \u2014 it is small and you will have it down in 10 minutes:</p>
          <ul>
            <li><strong>Bleeding</strong> \u2014 Bandages</li>
            <li><strong>Bruises</strong> \u2014 Medkit</li>
            <li><strong>Dehydration</strong> \u2014 IV Bag</li>
            <li><strong>Dried Eyes</strong> \u2014 Eye Drops</li>
            <li><strong>Flu</strong> \u2014 Cough Syrup</li>
            <li><strong>Headache</strong> \u2014 Medicine</li>
            <li><strong>High Fever</strong> \u2014 Cooling Gel</li>
            <li><strong>Low Sugar</strong> \u2014 Maple Syrup</li>
            <li><strong>Rashes</strong> \u2014 Ointment</li>
            <li><strong>Stomach Ache</strong> \u2014 Herbs</li>
          </ul>
          <blockquote><strong>Critical Warning:</strong> Dehydration is the exception \u2014 incorrect treatment is documented as fatal. If you are unsure, double-check the symptom before reaching for IV Bag. The wrong item on a Dehydrated patient can end a run.</blockquote>

          <h3>Bandages</h3>
          <p>The dedicated counter for the <strong>Bleeding</strong> condition. Single-condition item with a clear primary use. Spawns outside the Bleeding treatment room. One of the most straightforward items in the game \u2014 no dual-use, no special mechanics. Just grab and apply.</p>

          <h3>Cough Syrup</h3>
          <p>Treats the <strong>Flu</strong> condition. Single-use respiratory medication stocked in standard cabinets. Spawns outside the Flu treatment room. No secondary uses \u2014 this is a pure treatment item.</p>

          <h3>Cooling Gel</h3>
          <p>Topical gel for the <strong>High Fever</strong> condition. Provides rapid surface body temperature reduction. Spawns outside the Fever treatment room. One of the last treatment items you will unlock in the treatment pipeline.</p>

          <h3>Eye Drops</h3>
          <p>A <strong>dual-use</strong> item and one of the most versatile in the game. Primary: treats <strong>Dried Eyes</strong> condition. Secondary: pacifies the <strong>Mass of Eyes</strong> anomaly when applied directly. Also works as a <strong>Death Ritual cancel option</strong> \u2014 applying Eye Drops to the levitating patient ends the ritual with zero sanity loss. Always worth carrying one.</p>

          <h3>Herbs</h3>
          <p>Herbal mixture for the <strong>Stomach Ache</strong> condition. Single-use digestive distress treatment. <strong>One of the first two Shift 1 patients always requires Herbs</strong> \u2014 this is a predictable pattern you can rely on for early-game efficiency.</p>

          <h3>IV Bag</h3>
          <p>Fluid replacement for <strong>Dehydration</strong>. This is the most dangerous treatment item in the game because it requires an <strong>IV stand setup</strong> and takes time to administer. The wrong treatment on Dehydration can be <strong>fatal</strong> \u2014 possibly the only condition where a wrong item kills the patient outright rather than just failing to heal. Always confirm Dehydration before picking up the IV Bag.</p>

          <h3>Maple Syrup</h3>
          <p>The most versatile treatment item in Animal Hospital Anomaly. Primary: treats the <strong>Low Sugar</strong> condition. Secondary: <strong>bribes the Bed Monster</strong> \u2014 approach any bed with a crimson box underneath holding Maple Syrup and the monster takes the bribe instead of grabbing you. This is the <strong>only counter</strong> for the Monster Eating Patient emergency. <strong>Always carry at least one Maple Syrup from Shift 1 onward.</strong></p>

          <h3>Medicine</h3>
          <p>Generic pain reliever that treats the <strong>Headache</strong> condition. Standard cabinet stock. Single-purpose treatment item with no secondary uses.</p>

          <h3>Medkit</h3>
          <p>Treats <strong>Bruises</strong> \u2014 a blunt-trauma kit distinct from Bandages (which treat Bleeding) and Ointment (which treats Burns and Rashes). Easy to confuse with Bandages visually, but they treat different conditions. Check the label.</p>

          <h3>Ointment</h3>
          <p>A <strong>dual-use</strong> item. Primary: treats the <strong>Rashes</strong> condition. Secondary: serves as the <strong>manual fallback counter for Patient on Fire</strong> when no Fire Extinguisher is in reach. Slower than the extinguisher, but works. Spawns outside the treatment room.</p>'''
    },
    {
        "filename": "items-survival.html",
        "title": "Animal Hospital Anomaly Survival & Tool Items Guide: Weapons, Counters & Diagnostics",
        "description": "Complete survival and tool items guide for Animal Hospital Anomaly. Fire Extinguisher, Taser, Gun, Photo Camera, Flashlight, Mop, Smelling Salts, and Thermo \u2014 all 8 items explained.",
        "keywords": "Animal Hospital Anomaly survival items, Fire Extinguisher, Taser, Gun, Photo Camera, Flashlight, Mop, Smelling Salts, Thermo, weapons guide",
        "og_description": "Every survival tool and weapon explained \u2014 Fire Extinguisher, Taser, Gun, and the items that keep you alive.",
        "tag": "Items Guide",
        "date": "2026-07-01",
        "read": "9 min read",
        "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="equipment-guides.html">Equipment Guides</a><span>/</span><span class="current">Survival & Tool Items</span>',
        "content": '''<p>Survival and tool items are what keep you alive when anomalies break through. This category covers weapons, detection tools, and counters \u2014 the gear you reach for when a Skinwalker appears or a room catches fire. There are <strong>8 items</strong> in this category, ranging from free wall-mounted equipment to class-exclusive weapons.</p>

          <h3>Fire Extinguisher</h3>
          <p>The most important survival item in the game. This free pressurized canister handles three different threats:</p>
          <ul>
            <li><strong>Eliminates Hiders</strong> \u2014 the anomaly that hides in corners and dark areas</li>
            <li><strong>Removes Slime puddles</strong> \u2014 clears the floor hazard that slows movement</li>
            <li><strong>Extinguishes active fires</strong> \u2014 both Patient on Fire and Fire-in-Room</li>
            <li><strong>Eliminates Skinwalkers</strong> \u2014 the free-to-play counter for the most dangerous enemy</li>
          </ul>
          <p>The Fire Extinguisher has 100% charge that depletes with use and recharges at 1% per 2 seconds at its spawn location. Wall-mounted stations are located throughout the hospital hallways. <strong>Always carry one from Shift 2 onward.</strong> It is free, unlimited, and handles four different threats. There is no reason not to have one.</p>

          <h3>Photo Camera</h3>
          <p>The primary anomaly-detection tool. Issued at the admission window from the start of the game. The Photo Camera captures evidence invisible to the live monitor \u2014 snap a photo of every patient at intake and compare the photo to the live view. Mismatches reveal anomalies. Costs <strong>10 sanity per photo view</strong>, so do not spam it. Use it deliberately: photo at intake, check for discrepancies, move on.</p>

          <h3>Flashlight</h3>
          <p>Starter equipment that illuminates dark corners and reveals hidden anomalies under beds. Essential for the Bed Monster detection workflow \u2014 shine under every bed after admitting a patient. The Flashlight is always in your inventory from Shift 1 and does not take a slot. Use it reflexively.</p>

          <h3>Mop</h3>
          <p>A cleaning implement from the Utility Closet that removes Slime puddles. This is the <strong>only weapon that works on Slime</strong> \u2014 Fire Extinguisher does not clear it, weapons do not affect it. If you see green goo on the floor, get the Mop. Slime slows movement and can trap you during emergencies. Free from the Utility Closet.</p>

          <h3>Taser</h3>
          <p>The most reliable reusable weapon in the game. Instantly incapacitates Skinwalkers and other hostiles on contact. Available in two shop variants:</p>
          <ul>
            <li><strong>1-use Taser</strong> \u2014 $150 from the Supplies Shop (Shift 3+)</li>
            <li><strong>5-use Taser</strong> \u2014 $250 from the Supplies Shop (Shift 3+)</li>
            <li><strong>X-Taser (5-use)</strong> \u2014 Security class starter equipment</li>
          </ul>
          <p>The Taser is also the <strong>best Death Ritual cancel option</strong> \u2014 one zap ends the ritual instantly with zero sanity loss. If you have a Taser in inventory, the Death Ritual becomes a 2-second non-event.</p>

          <h3>Gun</h3>
          <p>The most powerful weapon in the game. Ranged, one-shot kill on Skinwalkers and most hostiles. 20 uses per unit. However, there are significant drawbacks:</p>
          <ul>
            <li><strong>Class-exclusive</strong> \u2014 only the Secret Agent class has access</li>
            <li><strong>Robux purchase</strong> \u2014 not available for in-game currency</li>
            <li><strong>Friendly-fire risk</strong> \u2014 shooting near patients or teammates causes them to faint or die</li>
            <li><strong>Noise effect</strong> \u2014 the gunshot sound causes nearby NPCs to faint from shock</li>
          </ul>
          <p>The community is split: Gun is preferred by paid players for range and reliability; Fire Extinguisher is the free-to-play alternative with more total uses. <strong>Never shoot near the intake area.</strong></p>

          <h3>Smelling Salts</h3>
          <p>A fast-acting stimulant that instantly wakes fainting patients. Counters both the <strong>Fainting Patient anomaly</strong> and the <strong>Patient Fainted emergency event</strong>. This turns a 60-second carry-and-transport into a 2-second instant fix. Relatively affordable from the Supplies Shop ($100-$150). Carry at least one from Shift 3 onward.</p>

          <h3>Thermo</h3>
          <p>A diagnostic tool that reads patient body temperature for <strong>High Fever confirmation</strong>. Diagnostic only \u2014 it does not treat anything. Use it when you suspect High Fever but need confirmation before administering Cooling Gel. Standard medical equipment, free to use.</p>'''
    },
    {
        "filename": "items-sanity.html",
        "title": "Animal Hospital Anomaly Sanity & Utility Items Guide: Chocolate, Coffee, Speed Cola & More",
        "description": "Complete sanity and utility items guide for Animal Hospital Anomaly. Chocolate vs Coffee efficiency comparison, Anti-Psychotics, Calming Meds, and Large Speed Cola strategy.",
        "keywords": "Animal Hospital Anomaly sanity items, Chocolate, Coffee, Anti-Psychotics, Calming Meds, Speed Cola, sanity management, utility consumables",
        "og_description": "Chocolate vs Coffee efficiency, Anti-Psychotics strategy, and when to use every sanity and utility item.",
        "tag": "Items Guide",
        "date": "2026-07-01",
        "read": "7 min read",
        "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="equipment-guides.html">Equipment Guides</a><span>/</span><span class="current">Sanity & Utility</span>',
        "content": '''<p>Sanity management is the invisible mechanic that determines whether you survive or wipe. Every anomaly, photo check, and failed emergency drains sanity. This guide covers all 5 sanity and utility consumables \u2014 what they do, how efficient they are, and when to use each one.</p>

          <h3>Chocolate</h3>
          <p>The <strong>most sanity-efficient restorative</strong> in Animal Hospital Anomaly. Each Chocolate bar provides:</p>
          <ul>
            <li><strong>20% sanity per bite</strong></li>
            <li><strong>3 bites per bar</strong></li>
            <li><strong>60% total recovery per bar</strong></li>
          </ul>
          <p>Chocolate is roughly <strong>4x more potent per use than Coffee</strong> (60% vs 15% total). It is the best single-purchase sanity item in the game. The trade-off is cost \u2014 Chocolate is more expensive than Coffee in the Supplies Shop. Use Chocolate when you need a large sanity recovery in one go (post-Ambulance Event, post-Death Ritual fail). Available from the Supplies Shop (Shift 3+).</p>

          <h3>Coffee</h3>
          <p>The most accessible sanity restorative. Each cup provides:</p>
          <ul>
            <li><strong>5% sanity per sip</strong></li>
            <li><strong>3 sips per cup</strong></li>
            <li><strong>15% total recovery per cup</strong></li>
          </ul>
          <p>Coffee is cheaper than Chocolate and more widely available, but less efficient per use. It also has a secondary function: <strong>applying Coffee to a Head Banger entity ends the encounter</strong>. This dual-use makes Coffee valuable beyond sanity management alone. The most cost-effective strategy: use Coffee for routine sanity maintenance, reserve Chocolate for emergency recovery.</p>

          <h3>Anti-Psychotics</h3>
          <p>A medication that <strong>slows the sanity decay rate</strong> rather than providing instant recovery. Anti-Psychotics are a maintenance item \u2014 use them at the start of high-anomaly shifts (Shift 4+) to reduce the baseline sanity drain from anomaly presence. The effect is gradual and stacks with other sanity management strategies. Best used proactively, not reactively. Available from the Supplies Shop.</p>

          <h3>Calming Meds</h3>
          <p>A strong medication that <strong>restores patient stability</strong>. This is the primary counter for the <strong>Mad Patient anomaly</strong>. When applied before surgical treatment, Calming Meds prevent the surgery fail-state that would otherwise kill the patient. This is a niche but critical item \u2014 if you encounter a Mad Patient without Calming Meds, the surgery will fail regardless of your minigame performance. Available from the Supplies Shop.</p>

          <h3>Large Speed Cola</h3>
          <p>A movement-speed consumable that increases your transit speed through the hospital. Essential for Ambulance Events and multi-emergency cascades where seconds matter. Sources:</p>
          <ul>
            <li><strong>Paramedic class starter</strong> \u2014 6 uses per shift</li>
            <li><strong>Vending Machine</strong> \u2014 scattered throughout the hospital</li>
            <li><strong>Supplies Shop</strong> \u2014 purchasable from Shift 3+</li>
          </ul>
          <p>Large Speed Cola does not affect carry speed reduction \u2014 you will still move slowly while carrying a fainted patient. But for everything else, the speed boost is significant. Prioritize buying this before known Ambulance shifts (Shift 4, 9, 14, etc.).</p>

          <h3>Sanity Management Strategy: Coffee vs Chocolate</h3>
          <p>The optimal approach is not "Coffee OR Chocolate" \u2014 it is using both for different situations:</p>
          <ul>
            <li><strong>Coffee for maintenance:</strong> Use when sanity is at 50-70% and you need a small top-up between patients. The 15% recovery is enough to keep you above the danger threshold without overspending.</li>
            <li><strong>Chocolate for emergencies:</strong> Use when sanity drops below 30% (post-cascade, post-encounter). The 60% recovery brings you back to safe levels in one item use.</li>
            <li><strong>Never let sanity drop below 20%:</strong> At sub-20% sanity, visual distortion effects kick in, making anomaly detection nearly impossible. This is a death spiral.</li>
          </ul>'''
    },
    {
        "filename": "items-upgrades.html",
        "title": "Animal Hospital Anomaly Shop Upgrades Guide: All 8 Permanent Upgrades with Costs & Priority",
        "description": "Complete shop upgrades guide for Animal Hospital Anomaly. All 8 permanent upgrades ranked by priority with Animal Coin costs, DNA Analysis, Extra Check-In Window, recovery speed, and more.",
        "keywords": "Animal Hospital Anomaly shop upgrades, permanent upgrades, DNA Analysis, Extra Check-In Window, Animal Coins, upgrade priority, Animal Hospital guide",
        "og_description": "All 8 permanent shop upgrades ranked by priority \u2014 which to buy first and how much Animal Coins each costs.",
        "tag": "Upgrades Guide",
        "date": "2026-07-01",
        "read": "8 min read",
        "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="equipment-guides.html">Equipment Guides</a><span>/</span><span class="current">Shop Upgrades</span>',
        "content": '''<p>Permanent shop upgrades are the primary long-term progression system in Animal Hospital (Anomaly). There are <strong>8 upgrades</strong> available from the Supplies Shop, which unlocks after Shift 3 and is run by the Shopkeeper Nurse. All upgrades persist across run resets and are purchased with <strong>Animal Coins</strong>, the game\'s premium currency.</p>

          <h3>Priority 1: 50% Faster DNA Analysis</h3>
          <p><strong>Cost:</strong> $110 Animal Coins | <strong>Effect:</strong> Halves DNA processing time from 9 seconds to 4.5 seconds.</p>
          <p>This is the <strong>consensus #1 upgrade</strong> in the Animal Hospital community. DNA Analysis is the bottleneck step in the patient pipeline \u2014 every patient goes through it, and halving the time speeds up every single patient you treat for the rest of your playtime. If you save for one upgrade first, make it this one. The return on investment is immediate and permanent.</p>

          <h3>Priority 2: Extra Check-In Window</h3>
          <p><strong>Cost:</strong> $190-200 Animal Coins | <strong>Effect:</strong> Opens a second admission window for simultaneous dual check-ins.</p>
          <p>The second most impactful upgrade because it doubles your intake throughput. During Ambulance Events (6+ simultaneous patients), two windows mean you can process two patients at once instead of queuing. <strong>Warning:</strong> this upgrade opens a new Head Banger spawn location at the second window. Be prepared for the additional threat. The trade-off is worth it for the throughput gain, but you must adjust your patrol route to cover both windows.</p>

          <h3>Priority 3: Patients Recover 25% Faster</h3>
          <p><strong>Cost:</strong> $115 Animal Coins | <strong>Effect:</strong> Reduces patient post-treatment recovery time from 35 seconds to approximately 26 seconds.</p>
          <p>Faster recovery means rooms free up faster for the next patient. During high-volume shifts, this directly translates to more patients treated per shift. Not as individually impactful as DNA Analysis, but it stacks multiplicatively with it \u2014 faster DNA + faster recovery = dramatically faster patient pipeline.</p>

          <h3>33% Faster Computers</h3>
          <p><strong>Cost:</strong> $110 Animal Coins | <strong>Effect:</strong> Computer processing time reduced 33% \u2014 2 seconds to approximately 1.3 seconds. Applies hospital-wide.</p>
          <p>A solid mid-tier upgrade. The 0.7-second reduction per computer interaction adds up over a full shift. Not flashy, but the cumulative time savings are significant across 5+ shifts. Buy this after the top 3 priorities.</p>

          <h3>Faster Check-In</h3>
          <p><strong>Cost:</strong> $250 Animal Coins | <strong>Effect:</strong> Skip the patient\'s self-introduction dialogue \u2014 forms are placed immediately upon arrival.</p>
          <p>The most expensive upgrade on this list. It reduces per-patient admission time by removing the dialogue sequence. Valuable for speed-running and high-efficiency play, but the high cost makes it a late-game purchase. Only buy this after you have the top 4 upgrades and are running Shift 10+ consistently.</p>

          <h3>+1 Carry Capacity</h3>
          <p><strong>Cost:</strong> $100 Animal Coins | <strong>Effect:</strong> Adds 1 inventory slot \u2014 moves you from the 3-slot baseline to 4 slots.</p>
          <p>An extra inventory slot means you can carry one more item per shift: Fire Extinguisher + Maple Syrup + Coffee + one flex slot. This flexibility is valuable, especially during Ambulance Events where you need multiple counter items. Available after Shift 3. One of the cheaper upgrades at $100.</p>

          <h3>NPC Speed Upgrade</h3>
          <p><strong>Cost:</strong> Tier 1 \u2014 $150 (+10%), Tier 2 \u2014 $250 (+12%, requires Tier 1) | <strong>Effect:</strong> Helper NPCs move faster.</p>
          <p>Patients visibly wear blue boots after Tier 1. Faster NPCs mean patients reach their beds faster and complete recovery faster. The effect is subtle but consistent. Tier 2 is expensive for a 2% increase over Tier 1 \u2014 buy Tier 1 for the visible speed boost and skip Tier 2 until you have coins to spare.</p>

          <h3>Treat From Inventory</h3>
          <p><strong>Cost:</strong> $450 Animal Coins | <strong>Effect:</strong> Skip the trip to the medicine cabinet \u2014 apply treatments directly from your inventory bar.</p>
          <p>The most expensive upgrade in the game and also the most dangerous. While it saves travel time, it introduces a critical risk: <strong>you can administer the wrong medication easily</strong> because you are selecting from your inventory bar rather than approaching a labeled cabinet. <strong>Only buy this after you trust your item-slot labelling completely.</strong> At $450, this is an endgame purchase for experienced players who never confuse Bandages with Medkit.</p>

          <h3>Recommended Purchase Order</h3>
          <ol>
            <li><strong>DNA Analysis ($110)</strong> \u2014 Highest impact, speeds every patient</li>
            <li><strong>Extra Check-In Window ($190-200)</strong> \u2014 Doubles intake capacity</li>
            <li><strong>Patients Recover 25% Faster ($115)</strong> \u2014 Frees rooms faster</li>
            <li><strong>+1 Carry Capacity ($100)</strong> \u2014 Extra item slot for emergencies</li>
            <li><strong>Faster Computers ($110)</strong> \u2014 Cumulative time savings</li>
            <li><strong>NPC Speed Tier 1 ($150)</strong> \u2014 Subtle but consistent</li>
            <li><strong>Faster Check-In ($250)</strong> \u2014 Late-game efficiency</li>
            <li><strong>Treat From Inventory ($450)</strong> \u2014 Endgame only, high risk</li>
          </ol>
          <blockquote>Save Animal Coins for DNA Analysis first. Everything else is secondary. Halving DNA processing time changes the pace of every shift from the moment you buy it.</blockquote>'''
    },
]

# Generate all 4 pages
for ev in pages:
    build_page(ev)
    print(f"Created: {ev['filename']}")

print(f"\nGenerated {len(pages)} item detail pages.")
