import os, sys
base_dir = r"C:\Users\tulia\animal-hospital-anomaly-guides"
domain = "https://animalhospitalanomalyguides.com"

# Read nav from boss-guides.html
with open(os.path.join(base_dir, "boss-guides.html"), "r", encoding="utf-8") as f:
    boss = f.read()
nav_start = boss.find("  <nav class=")
nav_end = boss.find("  </nav>", nav_start) + 8
nav = boss[nav_start:nav_end]

# Read footer from article-boss-fight-guide.html
with open(os.path.join(base_dir, "article-boss-fight-guide.html"), "r", encoding="utf-8") as f:
    art = f.read()
foot_start = art.find("  <footer class=")
foot_end = art.find("</html>", foot_start)
footer = art[foot_start:foot_end]

print(f"Nav: {len(nav)} chars, Footer: {len(footer)} chars")

def head(ev):
    ga = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-RESXT38T4M"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag("js", new Date());
      gtag("config", "G-RESXT38T4M");
    </script>"""
    return f"""    <meta charset="UTF-8">
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
{ga}
"""

import urllib.parse

def share_bar(ev):
    et = urllib.parse.quote(ev["title"])
    url = f"{domain}/{ev["filename"]}"
    return f"""        <!-- Share Bar -->
          <div class="share-bar">
            <span class="share-bar-label">Share this guide:</span>
            <a class="share-btn share-btn-x" href="https://x.com/intent/post?text={et}&url={url}" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>X</a>
            <a class="share-btn share-btn-facebook" href="https://www.facebook.com/sharer/sharer.php?u={url}" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>Facebook</a>
            <a class="share-btn share-btn-reddit" href="https://reddit.com/submit?url={url}&title={et}" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24"><path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0zm5.01 4.744c.688 0 1.25.561 1.25 1.249a1.25 1.25 0 0 1-2.498.056l-2.597-.547-.8 3.747c1.824.07 3.48.632 4.674 1.488.308-.309.73-.491 1.207-.491.968 0 1.754.786 1.754 1.754 0 .716-.435 1.333-1.01 1.614a3.111 3.111 0 0 1 .042.52c0 2.694-3.13 4.87-7.004 4.87-3.874 0-7.004-2.176-7.004-4.87 0-.183.015-.366.043-.534A1.748 1.748 0 0 1 4.028 12c0-.968.786-1.754 1.754-1.754.463 0 .898.196 1.207.49 1.207-.883 2.878-1.43 4.744-1.487l.885-4.182a.342.342 0 0 1 .14-.197.35.35 0 0 1 .238-.042l2.906.617a1.214 1.214 0 0 1 1.108-.701zM9.25 12C8.561 12 8 12.562 8 13.25c0 .687.561 1.248 1.25 1.248.687 0 1.248-.561 1.248-1.249 0-.688-.561-1.249-1.249-1.249zm5.5 0c-.687 0-1.248.561-1.248 1.25 0 .687.561 1.248 1.249 1.248.688 0 1.249-.561 1.249-1.249 0-.687-.562-1.249-1.25-1.249zm-5.466 3.99a.327.327 0 0 0-.231.094.33.33 0 0 0 0 .463c.842.842 2.484.913 2.961.913.477 0 2.105-.056 2.961-.913a.361.361 0 0 0 .029-.463.33.33 0 0 0-.464 0c-.547.533-1.684.73-2.512.73-.828 0-1.979-.196-2.512-.73a.326.326 0 0 0-.232-.095z"/></svg>Reddit</a>
            <button class="share-btn share-btn-copy" data-url="{url}"><svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg><span class="share-btn-text">Copy Link</span></button>
          </div>"""

def build_page(ev):
    h = head(ev)
    sb = share_bar(ev)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{h}
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
              <li><a href="boss-guides.html">Events &amp; Emergencies \u2014 Full Timer Reference</a></li>
              <li><a href="character-guides.html">Anomaly &amp; Enemy Guide \u2014 All Entities</a></li>
              <li><a href="equipment-guides.html">Items &amp; Shop Upgrades \u2014 Best Gear</a></li>
              <li><a href="article-how-to-survive.html">How to Survive \u2014 14 Reflex Tips</a></li>
            </ul>
          </div>
        </div>
{sb}
      </article>
      <div class="ad-placeholder ad-placeholder-bottom" aria-label="Advertisement"></div>
    </div>
  </main>
{footer}
</body>
</html>"""
    filepath = os.path.join(base_dir, ev["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    return filepath

print("Functions defined. Ready.")


# ===== EVENT CONTENT DATA =====
events = []

events.append({
    "filename": "event-ambulance.html",
    "title": "Ambulance Event Guide: Survive the 6+ Patient Surge in Animal Hospital Anomaly",
    "description": "Complete Ambulance Event guide for Animal Hospital Anomaly. 6+ patient surge strategy, triage order, loadout checklist, and how to survive every 5th shift on Roblox.",
    "keywords": "Animal Hospital Anomaly Ambulance Event, ambulance surge guide, Animal Hospital shift 4, multi-patient triage, Animal Hospital Anomaly emergency guide",
    "og_description": "Survive the Ambulance Event with our triage order, pre-shift loadout, and cascade management strategies.",
    "tag": "Event Guide",
    "date": "2026-07-01",
    "read": "8 min read",
    "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="boss-guides.html">Boss Guides</a><span>/</span><span class="current">Ambulance Event</span>',
    "content": """<p>The Ambulance Event is the most chaotic encounter in Animal Hospital (Anomaly). Debuting at <strong>Shift 4</strong> and re-firing every fifth shift thereafter, it floods your hospital with 6+ patients simultaneously while Dr. Harlow announces an anomaly attack over the intercom. Multiple emergencies can stack on top of each other within the surge, creating a cascade that tests every skill you have developed.</p>
          <h3>When Does the Ambulance Event Trigger?</h3>
          <p>The first Ambulance Event always hits at <strong>Shift 4</strong>. After that, it recurs every 5 shifts like clockwork: Shift 9, Shift 14, Shift 19, and so on. Plan your loadout and sanity management around these intervals. If you are low on supplies or sanity heading into a multiple-of-5 shift, you are in trouble.</p>
          <h3>The Triage Order \u2014 Who to Treat First</h3>
          <p>When 6+ patients arrive simultaneously, you cannot treat everyone at once. Follow this triage order exactly:</p>
          <ol><li><strong>Burning patients first</strong> \u2014 The 60-second Patient on Fire timer is the tightest in the game. Fire Extinguisher immediately upon spotting flames.</li>
          <li><strong>Critical Patient timers</strong> \u2014 100-120 seconds but requires the full treatment chain (diagnose, procure, administer, monitor). Start these early because the chain takes time.</li>
          <li><strong>Skinwalker conversions</strong> \u2014 Any anomaly you miss during the intake panic converts to a Skinwalker. Handle these as combat encounters. Taser or Fire Extinguisher.</li>
          <li><strong>Stable admissions</strong> \u2014 Last. These patients can wait while you handle the active crises.</li></ol>
          <h3>The Cascade Problem</h3>
          <p>The trap is treating the Ambulance Event as the same as a normal shift but faster. It is not. Multiple emergencies can fire simultaneously: Fire-in-Room + Patient Fainted + Critical Patient at once is plausible and has happened to experienced players. The key pattern: <strong>resolve the hazard that is actively damaging things first, then the one that is just on a timer.</strong> A burning room can knock standing patients into the fainted state, creating a spiral.</p>
          <h3>Pre-Ambulance Loadout Checklist</h3>
          <ul><li><strong>Fire Extinguisher</strong> \u2014 Non-negotiable. Handles Patient on Fire and Fire-in-Room. Refill at wall stations between waves.</li>
          <li><strong>Maple Syrup</strong> \u2014 Non-negotiable. Handles Bed Monster events during the chaos. Carry at least one.</li>
          <li><strong>Coffee (x2)</strong> \u2014 Sanity management during extended crisis. The Ambulance Event can drain 20-30 sanity points if things cascade.</li>
          <li><strong>Chocolate</strong> \u2014 Emergency sanity restore. Use when Coffee runs out.</li>
          <li><strong>Taser (5-use)</strong> \u2014 For Skinwalker conversions during the panic.</li>
          <li><strong>Large Speed Cola</strong> \u2014 If your budget allows. Transit speed between cascading emergencies makes a huge difference.</li></ul>
          <h3>Common Failure Points</h3>
          <ul><li><strong>Skipping intake checks</strong> \u2014 The panic makes you want to speed through window checks. Do not. A missed anomaly becomes a Skinwalker that kills a patient and drains sanity.</li>
          <li><strong>Treating stable patients first</strong> \u2014 Triage order exists for a reason. Burning and Critical patients have hard timers. Stable patients can wait.</li>
          <li><strong>Empty inventory</strong> \u2014 Going into a known Ambulance shift with no Fire Extinguisher, no Maple Syrup, and no sanity items is a guaranteed wipe.</li>
          <li><strong>Ignoring sanity</strong> \u2014 The Ambulance Event drains sanity fast through multiple overlapping sources. If you drop below 30 sanity, you will start making worse decisions.</li></ul>
          <blockquote>The Ambulance Event is not a test of speed. It is a test of triage. Know the priority order, carry the right items, and do not panic-check patients at the window.</blockquote>"""
})

print(f"Events data loaded: {len(events)} event(s)")
# Generate all pages
for ev in events:
    path = build_page(ev)
    print(f"Created: {ev['filename']}")
print(f"Done! Generated {len(events)} page(s).")

events.append({
    "filename": "event-patient-fire.html",
    "title": "Patient on Fire Emergency Guide: 60-Second Counter in Animal Hospital Anomaly",
    "description": "Patient on Fire emergency guide for Animal Hospital Anomaly. How to extinguish burning patients, Fire Extinguisher vs Ointment, sanity drain, and timer details.",
    "keywords": "Animal Hospital Anomaly Patient on Fire, burning patient guide, Fire Extinguisher counter, Animal Hospital emergency timer, Patient on Fire 60 seconds",
    "og_description": "Put out burning patients fast with the right counter and learn how the 60-second timer works in Animal Hospital Anomaly.",
    "tag": "Emergency Guide",
    "date": "2026-07-01",
    "read": "6 min read",
    "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="boss-guides.html">Boss Guides</a><span>/</span><span class="current">Patient on Fire</span>',
    "content": """<p>The Patient on Fire emergency is one of the most visually alarming crises in Animal Hospital (Anomaly). A burning patient sprints through the hospital corridors trailing flames, and you have exactly <strong>60 seconds</strong> to extinguish them before they die. Every second they burn drains <strong>-1 sanity/second</strong> from everyone in proximity, making this a dual threat: the timer and the sanity drain.</p>
          <h3>How It Triggers</h3>
          <p>Patient on Fire can trigger in three ways:</p>
          <ul><li><strong>Random emergency spawn</strong> \u2014 Starting Shift 3, this emergency can fire randomly during any shift.</li>
          <li><strong>Ambulance Event cascade</strong> \u2014 During the 6+ patient surge, burning patients can appear among the arrivals.</li>
          <li><strong>Fire-in-Room proximity</strong> \u2014 A patient standing in a burning room for too long will catch fire themselves, creating a secondary emergency.</li></ul>
          <h3>The 60-Second Timer</h3>
          <p>From the moment flames appear on the patient, the clock starts. 60 seconds is tight but manageable if you react immediately. The patient will sprint randomly through the hospital, potentially spreading the emergency to multiple rooms. Do not chase aimlessly \u2014 equip your counter item first, then intercept.</p>
          <h3>Counter Options Ranked</h3>
          <ol><li><strong>Fire Extinguisher</strong> \u2014 The one-shot counter. One spray and the fire is out. No sanity cost. Unlimited refills at wall stations. This is the definitive solution.</li>
          <li><strong>Ointment</strong> \u2014 The manual fallback. Applies burn treatment to the patient. Slower than the Fire Extinguisher and consumes the item, but works if you have no extinguisher.</li></ol>
          <p>Do not try anything else. Shooting or tasing a burning patient kills them and counts as a failed emergency. Only the Fire Extinguisher or Ointment resolves this correctly.</p>
          <h3>Sanity Management After Extinguishing</h3>
          <p>The burning patient drains -1 sanity/second from everyone within a certain radius. After resolving the fire:</p>
          <ul><li>Check your sanity immediately. If below 40, use Coffee or Chocolate.</li>
          <li>Check if the fire spawned a secondary Fire-in-Room event in any rooms the burning patient passed through.</li>
          <li>Scan for fainted patients \u2014 the sanity shock can knock low-sanity NPCs into the fainted state.</li></ul>
          <h3>Can Patient on Fire Be an Anomaly?</h3>
          <p>Yes. A patient arriving at the window already on fire is likely an anomaly manifestation rather than a random emergency. These patients should be rejected at intake. Check the patient sheet: if the photo shows a normal-looking patient but the live view shows flames, reject immediately.</p>"""
})

events.append({
    "filename": "event-death-ritual.html",
    "title": "Death Ritual Emergency Guide: 4 Counter Options in Animal Hospital Anomaly",
    "description": "Death Ritual emergency guide for Animal Hospital Anomaly. Complete counter options ranked \u2014 Taser, Defibrillator, Eye Drops, kicking candles \u2014 with timer details and sanity costs.",
    "keywords": "Animal Hospital Anomaly Death Ritual, ritual counter guide, Death Ritual timer, candle kicking sanity cost, Taser ritual cancel, Animal Hospital emergency guide",
    "og_description": "Cancel the Death Ritual with any of 4 counter methods \u2014 ranked from fastest (Taser) to last-resort (candle kicking).",
    "tag": "Emergency Guide",
    "date": "2026-07-01",
    "read": "7 min read",
    "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="boss-guides.html">Boss Guides</a><span>/</span><span class="current">Death Ritual</span>',
    "content": """<p>The Death Ritual is the most dramatic emergency in Animal Hospital (Anomaly). A patient levitates above their bed surrounded by ritual candles, a timer starts ticking, and failure means the patient dies. But unlike other emergencies with a single counter, the Death Ritual gives you <strong>four different ways</strong> to cancel it \u2014 each with different speed, cost, and requirements.</p>
          <h3>What Is the Death Ritual?</h3>
          <p>Visually, the patient floats in the air with dark ritual candles arranged around the bed. A timer appears (30-60 seconds depending on source \u2014 patches may have changed the duration). If the timer expires without cancellation, the patient dies and you lose significant sanity.</p>
          <h3>How It Triggers</h3>
          <p>The Death Ritual has a specific trigger condition: <strong>admitting a Hollow Face anomaly</strong>. Hollow Face patients have dark hollow eyes, twitching motions, and a hunched posture. If you admit one at the intake window, they will eventually trigger the Death Ritual from their hospital bed. This is 100% preventable \u2014 always check for Hollow Face visual tells at intake.</p>
          <h3>Counter Options Ranked by Efficiency</h3>
          <ol><li><strong>Tase the patient</strong> \u2014 No sanity loss. Instant cancel. Requires Taser in inventory. This is the best option if you have a Taser.</li>
          <li><strong>Defibrillate</strong> \u2014 Instant cancel. Requires access to Room 7 (Heart Monitor room). Fastest if you are near Room 7. No sanity cost.</li>
          <li><strong>Apply Eye Drops / IV Drops / Coffee</strong> \u2014 Cancels the ritual on application. Costs the item but no sanity loss. Good middle-ground option.</li>
          <li><strong>Kick all candles</strong> \u2014 1-3 sanity cost per candle kicked. Must extinguish ALL candles within the timer window. Slowest and most sanity-costly. Last resort.</li></ol>
          <h3>The Timer Controversy</h3>
          <p>Community sources disagree on the Death Ritual timer: some report 30 seconds, others 60 seconds. This may vary by patch version. <strong>Treat 30 seconds as the safe planning number.</strong> That gives you comfortable margin regardless of which version you are playing.</p>
          <h3>Prevention</h3>
          <p>Reject Hollow Face patients at the window. Check for dark hollow eyes, twitching body movements, and hunched posture during the visual intake check. A quick CCTV check will also reveal the hollow face feature. Preventing the ritual is always better than countering it.</p>"""
})

events.append({
    "filename": "event-critical-patient.html",
    "title": "Critical Patient Emergency Guide: Full Treatment Chain in Animal Hospital Anomaly",
    "description": "Critical Patient emergency guide for Animal Hospital Anomaly. 100-120 second timer, full treatment chain walkthrough, ambulance wave strategy, and triage priorities.",
    "keywords": "Animal Hospital Anomaly Critical Patient, critical patient timer, treatment chain guide, ambulance triage, Animal Hospital emergency counter",
    "og_description": "Master the Critical Patient emergency \u2014 the only timed event that requires the full treatment chain under pressure.",
    "tag": "Emergency Guide",
    "date": "2026-07-01",
    "read": "7 min read",
    "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="boss-guides.html">Boss Guides</a><span>/</span><span class="current">Critical Patient</span>',
    "content": """<p>The Critical Patient emergency is widely considered the hardest timed crisis in Animal Hospital (Anomaly). Unlike other emergencies that require a single action, the Critical Patient needs the <strong>entire treatment chain</strong>: diagnose, procure, administer, monitor. And you have 100-120 seconds to do it while other things are likely on fire.</p>
          <h3>How It Triggers</h3>
          <p>Critical Patients appear during <strong>ambulance waves</strong> starting Shift 4. Each ambulance wave can bring one or more Critical Patients, each with their own independent per-arrival timer. The timer starts the moment the patient enters the hospital \u2014 not when you first interact with them.</p>
          <h3>The 100-120 Second Timer</h3>
          <p>The timer varies: most Critical Patients have 100-120 seconds, but some can have as little as 60 seconds. If the timer expires, the patient dies. There is no partial credit \u2014 the full treatment chain must complete before the timer hits zero.</p>
          <h3>The Full Treatment Chain</h3>
          <ol><li><strong>Diagnose</strong> \u2014 Examine the patient and identify the condition. This step takes 3-5 seconds if you know what to look for.</li>
          <li><strong>Procure</strong> \u2014 Go to the appropriate supply room and fetch the treatment item. Room location matters \u2014 know your hospital layout.</li>
          <li><strong>Administer</strong> \u2014 Apply the treatment to the patient. Antibiotics for Infection, Bandages for Injury, Cold Pack for Fever, etc. Using the wrong item wastes time.</li>
          <li><strong>Monitor</strong> \u2014 Wait for the treatment to take effect. The patient must stabilise before the timer expires.</li></ol>
          <h3>Why Critical Patient Is the Hardest Emergency</h3>
          <p>Other emergencies need one action. Patient on Fire? Spray extinguisher. Death Ritual? Tase. But the Critical Patient requires four sequential steps that cannot be skipped or accelerated (other than movement speed). This means you are locked into a multi-step process while other emergencies may be firing simultaneously. Preparation is everything: know the hospital layout, pre-stock common treatment items, and triage before the timer starts.</p>"""
})

events.append({
    "filename": "event-surgery-monster.html",
    "title": "Surgery Monster (Tendril) Guide: 45-Second Room 8 Minigame in Animal Hospital Anomaly",
    "description": "Surgery Monster emergency guide for Animal Hospital Anomaly. Room 8 Tendril encounter, 45-second surgery minigame solution, tool matching strategy, and what NOT to do.",
    "keywords": "Animal Hospital Anomaly Surgery Monster, Room 8 Tendril, surgery minigame guide, purple monster guide, Animal Hospital boss guide",
    "og_description": "Beat the Surgery Monster in Room 8 with our 45-second minigame strategy \u2014 and learn why shooting kills the patient.",
    "tag": "Emergency Guide",
    "date": "2026-07-01",
    "read": "7 min read",
    "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="boss-guides.html">Boss Guides</a><span>/</span><span class="current">Surgery Monster</span>',
    "content": """<p>The Surgery Monster (also called the Tendril) is the tightest timer in Animal Hospital (Anomaly). Purple tentacles emerge from the operating table during Room 8 surgery, and you have exactly <strong>45 seconds</strong> to complete the surgery minigame while the monster threatens to smother the patient. This is the only emergency where combat makes things worse.</p>
          <h3>When and Where It Appears</h3>
          <p>The Surgery Monster triggers exclusively in <strong>Room 8 (Surgery)</strong> during patient recovery. It can appear randomly from Shift 3 onwards, with increased frequency in later shifts. The monster manifests as purple-black tendrils rising from the operating table, wrapping around the patient body.</p>
          <h3>What NOT to Do</h3>
          <ul><li><strong>Do NOT shoot the monster</strong> \u2014 The Gun kills the patient, not the monster.</li>
          <li><strong>Do NOT tase the monster</strong> \u2014 Same result as shooting. The patient dies.</li>
          <li><strong>Do NOT leave Room 8</strong> \u2014 You cannot re-enter mid-surgery. If you leave, the patient is lost.</li>
          <li><strong>Do NOT panic</strong> \u2014 45 seconds is enough time if you know the minigame.</li></ul>
          <h3>The 45-Second Surgery Minigame Strategy</h3>
          <ol><li><strong>Know the tool before entering</strong> \u2014 Check the patient condition at intake. Each condition maps to specific surgery tools.</li>
          <li><strong>Scan the tool layout immediately</strong> \u2014 Tool positions are randomised per shift. Your first 2-3 seconds should identify where each tool is.</li>
          <li><strong>Match prompts in order</strong> \u2014 The minigame is sequential. Do not click ahead.</li>
          <li><strong>Complete all prompts</strong> \u2014 Typically 4-6 prompts in a full surgery. Partial completion does not count.</li></ol>
          <h3>Room 8 Cross-Hazard Problem</h3>
          <p>Room 8 is the most dangerous room because multiple hazards can fire simultaneously during surgery: Fire-in-Room, Bed Monster spawns, and Patient Fainted from sanity shock. Always carry Fire Extinguisher and Maple Syrup before entering Room 8.</p>
          <blockquote>The Surgery Monster is not a combat encounter. It is a performance test under pressure. Prepare your tools, know the layout, and do not shoot the patient.</blockquote>"""
})

print(f"Added 4 more events. Total: {len(events)}")

events.append({
    "filename": "event-monster-eating.html",
    "title": "Monster Eating Patient Guide: 30-Second Maple Syrup Counter in Animal Hospital Anomaly",
    "description": "Monster Eating Patient emergency guide for Animal Hospital Anomaly. 30-second timer, Maple Syrup counter, Bed Monster escalation, and how to react immediately.",
    "keywords": "Animal Hospital Anomaly Monster Eating Patient, Bed Monster eating guide, Maple Syrup counter, 30 second emergency, Animal Hospital quick reaction guide",
    "og_description": "React to the Monster Eating Patient emergency in under 10 seconds with the only counter that works \u2014 Maple Syrup.",
    "tag": "Emergency Guide",
    "date": "2026-07-01",
    "read": "5 min read",
    "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="boss-guides.html">Boss Guides</a><span>/</span><span class="current">Monster Eating Patient</span>',
    "content": """<p>The Monster Eating Patient emergency has the <strong>shortest timer in the game</strong>: 30 seconds. If you do not react within roughly 10 seconds, the patient is consumed and the emergency is failed. This guide covers the only counter that works, how the emergency escalates from the Bed Monster, and the reflex you need to build.</p>
          <h3>Trigger Condition: Ignored Bed Monster</h3>
          <p>The Monster Eating Patient is not a standalone random emergency. It is a <strong>direct escalation</strong> of an ignored Bed Monster. The chain: a Bed Monster spawns under a patient bed, you do not check or do nothing, the Bed Monster activates and grabs the patient, and the 30-second timer begins. This means the emergency is <strong>100% avoidable</strong> if you check under every bed after admitting a patient and apply Maple Syrup preemptively.</p>
          <h3>The 30-Second Timer</h3>
          <p>Thirty seconds is the shortest timer in the game. Realistically, you have about <strong>10 seconds of reaction time</strong> before the remaining time becomes uncomfortably tight. If you are on the other side of the hospital, you may not make it. This is why prevention is so important.</p>
          <h3>Counter: Maple Syrup Only</h3>
          <p>There is exactly one counter: <strong>Maple Syrup</strong>. Approach the bed holding Maple Syrup and interact \u2014 the monster takes the syrup as a bribe instead of consuming the patient. One application ends the emergency immediately with zero sanity loss.</p>
          <p>What does NOT work: shooting (kills the patient), tasing (kills the patient), Fire Extinguisher (no effect), any other item (no effect).</p>
          <h3>Prevention: The Bed Check Reflex</h3>
          <p>Build this reflex: after every patient is admitted and assigned to a bed, <strong>immediately check under that bed</strong>. Look for the crimson box with black hands and red eyes. If present, apply Maple Syrup before the monster activates. Carry at least one Maple Syrup at all times from Shift 1 onwards.</p>"""
})

events.append({
    "filename": "event-fire-in-room.html",
    "title": "Fire in Room Emergency Guide: Sanity Drain and Extinguisher Counter in Animal Hospital Anomaly",
    "description": "Fire in Room emergency guide for Animal Hospital Anomaly. Sanity drain rate, Fire Extinguisher counter, fainted patient cascade, Skinwalker reveal mechanic, and room safety.",
    "keywords": "Animal Hospital Anomaly Fire in Room, room fire guide, Fire Extinguisher counter, sanity drain fire, Skinwalker reveal, Animal Hospital fire emergency",
    "og_description": "Extinguish room fires fast, manage the sanity drain, and use the fire to identify hidden Skinwalkers.",
    "tag": "Event Guide",
    "date": "2026-07-01",
    "read": "6 min read",
    "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="boss-guides.html">Boss Guides</a><span>/</span><span class="current">Fire in Room</span>',
    "content": """<p>Fire in Room is classified as an <strong>event</strong> rather than a timed emergency \u2014 there is no hard fail timer, but the continuous -1 sanity/second drain makes it dangerous if ignored. It also has a unique mechanic: patients entering a burning room and NOT fainting are revealed as Skinwalkers.</p>
          <h3>How It Triggers</h3>
          <p>Room fires can start in several ways: a Patient on Fire sprinting through rooms (most common), random event spawn from Shift 3, or rare electrical failure sparking multiple rooms simultaneously.</p>
          <h3>Sanity Drain and Cascade Effects</h3>
          <p>A burning room drains -1 sanity/second from everyone inside or adjacent. Key cascade effects:</p>
          <ul><li><strong>New patients entering a burning room faint immediately</strong> \u2014 You lose that patient to the fainted state.</li>
          <li><strong>Patients who enter WITHOUT fainting are Skinwalkers</strong> \u2014 This is 100% certainty identification without visual checks.</li>
          <li><strong>Standing patients near fire eventually catch fire themselves</strong> \u2014 Creating secondary Patient on Fire emergencies.</li></ul>
          <h3>Counter: Fire Extinguisher</h3>
          <p>The Fire Extinguisher is the only counter. One spray extinguishes the room fire completely. Extinguishers are at wall stations throughout the hospital with infinite refills. After extinguishing, check for fainted patients and your sanity level.</p>
          <h3>The Skinwalker Reveal Mechanic</h3>
          <p>This is the most under-utilised mechanic in the game: normal patients faint in burning rooms, but Skinwalkers walk through fire unaffected. If you suspect a patient is a Skinwalker but cannot confirm via visual checks, lure them into a burning room. If they keep walking, tase them immediately.</p>"""
})

events.append({
    "filename": "event-patient-fainted.html",
    "title": "Patient Fainted Emergency Guide: 60-Second Carry Counter in Animal Hospital Anomaly",
    "description": "Patient Fainted emergency guide for Animal Hospital Anomaly. 60-second timer, designated bed carry, Smelling Salts fast counter, fire and gunshot triggers, and cascade management.",
    "keywords": "Animal Hospital Anomaly Patient Fainted, fainted carry guide, Smelling Salts counter, designated bed, Animal Hospital fainted emergency",
    "og_description": "Carry fainted patients to the designated bed within 60 seconds, or use Smelling Salts for the instant recovery.",
    "tag": "Emergency Guide",
    "date": "2026-07-01",
    "read": "5 min read",
    "breadcrumb": '<a href="index.html">Home</a><span>/</span><a href="boss-guides.html">Boss Guides</a><span>/</span><span class="current">Patient Fainted</span>',
    "content": """<p>The Patient Fainted emergency is unique because it requires a <strong>physical carry</strong> to resolve. A patient collapses and you must transport them from wherever they fell to a designated recovery bed within 60 seconds. It is not the hardest emergency, but during an Ambulance cascade, carrying a patient while other timers are ticking is where runs fall apart.</p>
          <h3>Trigger Conditions</h3>
          <p>Patients can faint from check-in stress, fire contact, gunshot proximity, or extreme sanity shock events. Firing the Gun near patients causes them to faint from the noise shock \u2014 never shoot near the intake area.</p>
          <h3>The 60-Second Timer and Carry Mechanic</h3>
          <p>From the moment a patient collapses, you have 60 seconds to pick them up and place them on a designated recovery bed. The timer stops the moment the patient is placed. While carrying, you cannot use any other items or weapons. Movement speed is reduced. If the timer expires, the patient dies.</p>
          <h3>Counter Options</h3>
          <ol><li><strong>Smelling Salts (fast counter)</strong> \u2014 Apply to the fainted patient for instant recovery on the spot. No carry required. Preferred method.</li>
          <li><strong>Manual carry (standard counter)</strong> \u2014 Pick up and transport to the designated bed. Takes 5-15 seconds. Always the fallback option.</li></ol>
          <h3>Cascade Risk During Ambulance Events</h3>
          <p>During Ambulance Events, multiple patients can faint simultaneously from fire/sanity shock. Carrying a patient makes you unable to counter other active emergencies. Always prioritise active damage (fire) over timed transport (carry). Smelling Salts are relatively affordable ($100-$150) \u2014 carry at least one from Shift 3 onwards to turn a 60-second transport into a 2-second instant fix.</p>"""
})


# ===== UPDATE all-articles.html, index.html, sitemap.xml =====
import os

base_dir = r"C:\Users\tulia\animal-hospital-anomaly-guides"

new_articles_html = '''
          <div class="article-item">
            <div class="article-item-content">
              <span class="article-item-tag">Emergency Guide</span>
              <h3><a href="event-ambulance.html">Ambulance Event Guide: Survive the 6+ Patient Surge</a></h3>
              <p>Ambulance Event triage order, pre-shift loadout checklist, cascade management, and how to survive every 5th shift.</p>
            </div>
            <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
          </div>
          <div class="article-item">
            <div class="article-item-content">
              <span class="article-item-tag">Emergency Guide</span>
              <h3><a href="event-patient-fire.html">Patient on Fire Guide: 60-Second Counter</a></h3>
              <p>How to extinguish burning patients, Fire Extinguisher vs Ointment, sanity drain details, and timer breakdown.</p>
            </div>
            <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
          </div>
          <div class="article-item">
            <div class="article-item-content">
              <span class="article-item-tag">Emergency Guide</span>
              <h3><a href="event-death-ritual.html">Death Ritual Guide: 4 Counter Options</a></h3>
              <p>All four ways to cancel the Death Ritual \u2014 Taser, Defibrillator, Eye Drops, and candle kicking \u2014 ranked by speed and cost.</p>
            </div>
            <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
          </div>
          <div class="article-item">
            <div class="article-item-content">
              <span class="article-item-tag">Emergency Guide</span>
              <h3><a href="event-critical-patient.html">Critical Patient Guide: Full Treatment Chain</a></h3>
              <p>Master the hardest emergency \u2014 100-120 second timer, full treatment chain walkthrough, and triage priorities.</p>
            </div>
            <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
          </div>
          <div class="article-item">
            <div class="article-item-content">
              <span class="article-item-tag">Emergency Guide</span>
              <h3><a href="event-surgery-monster.html">Surgery Monster Guide: 45-Second Room 8 Minigame</a></h3>
              <p>Room 8 Tendril encounter, surgery minigame strategy, tool matching, and what NOT to do.</p>
            </div>
            <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
          </div>
          <div class="article-item">
            <div class="article-item-content">
              <span class="article-item-tag">Emergency Guide</span>
              <h3><a href="event-monster-eating.html">Monster Eating Patient Guide: 30-Second Counter</a></h3>
              <p>Shortest timer in the game. Maple Syrup counter, Bed Monster escalation chain, and the bed-check reflex.</p>
            </div>
            <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
          </div>
          <div class="article-item">
            <div class="article-item-content">
              <span class="article-item-tag">Event Guide</span>
              <h3><a href="event-fire-in-room.html">Fire in Room Guide: Sanity Drain &amp; Skinwalker Reveal</a></h3>
              <p>Room fire strategy, sanity drain rate, fainted patient cascade, and the Skinwalker reveal mechanic.</p>
            </div>
            <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
          </div>
          <div class="article-item">
            <div class="article-item-content">
              <span class="article-item-tag">Emergency Guide</span>
              <h3><a href="event-patient-fainted.html">Patient Fainted Guide: 60-Second Carry Counter</a></h3>
              <p>Carry to designated bed within 60 seconds or use Smelling Salts for instant recovery. Cascade management tips.</p>
            </div>
            <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
          </div>
'''

# --- Update all-articles.html ---
art_path = os.path.join(base_dir, "all-articles.html")
with open(art_path, "r", encoding="utf-8") as f:
    art_text = f.read()

insert_marker = '<h3><a href="article-boss-fight-guide.html">Boss Fight Guide'
idx = art_text.find(insert_marker)
if idx >= 0:
    # Find end of this article-item block
    block_end = art_text.find('</div>', art_text.find('card-meta', idx))
    block_end = art_text.find('</div>', block_end + 6)
    # Insert after this block
    new_text = art_text[:block_end+6] + "\n" + new_articles_html + art_text[block_end+6:]
    with open(art_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"Updated all-articles.html (+8 articles)")
else:
    print("ERROR: Could not find insertion point in all-articles.html")

# --- Update index.html (homepage article cards) ---
# First read index.html
idx_path = os.path.join(base_dir, "index.html")
with open(idx_path, "r", encoding="utf-8") as f:
    idx_text = f.read()

# The index.html has article cards. Let me add the new event pages after the existing article cards in the #articles section
# Find the last article card in the articles section
marker2 = '<h3><a href="article-how-to-survive.html">'
idx2 = idx_text.find(marker2)
if idx2 >= 0:
    block_end2 = idx_text.find('</div>', idx_text.find('card-meta', idx2))
    block_end2 = idx_text.find('</div>', block_end2 + 6)
    
    homepage_cards = '''
            <article class="article-item">
              <span class="article-item-tag">Emergency Guide</span>
              <h3><a href="event-ambulance.html">Ambulance Event Guide: Survive the 6+ Patient Surge</a></h3>
              <p>Triage order, pre-shift loadout, and cascade management for the hardest encounter.</p>
              <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
            </article>
            <article class="article-item">
              <span class="article-item-tag">Emergency Guide</span>
              <h3><a href="event-death-ritual.html">Death Ritual Guide: 4 Counter Options</a></h3>
              <p>All four ways to cancel the Death Ritual ranked by speed, cost, and requirements.</p>
              <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
            </article>
            <article class="article-item">
              <span class="article-item-tag">Emergency Guide</span>
              <h3><a href="event-surgery-monster.html">Surgery Monster Guide: 45-Second Minigame</a></h3>
              <p>Room 8 Tendril encounter strategy, tool matching, and cross-hazard management.</p>
              <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
            </article>
            <article class="article-item">
              <span class="article-item-tag">Emergency Guide</span>
              <h3><a href="event-patient-fire.html">Patient on Fire Guide: 60-Second Counter</a></h3>
              <p>Extinguisher vs Ointment, sanity drain details, and how to handle burning patients fast.</p>
              <span class="card-meta"><time datetime="2026-07-01">Jul 1, 2026</time></span>
            </article>
'''
    new_idx_text = idx_text[:block_end2+6] + "\n" + homepage_cards + idx_text[block_end2+6:]
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(new_idx_text)
    print(f"Updated index.html (+4 homepage cards)")
else:
    print("ERROR: Could not find insertion point in index.html")

# --- Update sitemap.xml ---
sitemap_path = os.path.join(base_dir, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sm_text = f.read()

sitemap_entries = """
  <!-- Emergency Detail Pages -->
  <url>
    <loc>https://animalhospitalanomalyguides.com/event-ambulance.html</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://animalhospitalanomalyguides.com/event-patient-fire.html</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://animalhospitalanomalyguides.com/event-death-ritual.html</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://animalhospitalanomalyguides.com/event-critical-patient.html</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://animalhospitalanomalyguides.com/event-surgery-monster.html</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://animalhospitalanomalyguides.com/event-monster-eating.html</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://animalhospitalanomalyguides.com/event-fire-in-room.html</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://animalhospitalanomalyguides.com/event-patient-fainted.html</loc>
    <lastmod>2026-07-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""

# Insert before </urlset>
close_tag = "</urlset>"
sm_text = sm_text.replace(close_tag, sitemap_entries + "\n" + close_tag)
with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sm_text)
print("Updated sitemap.xml (+8 URLs)")

print("\nAll updates complete!")