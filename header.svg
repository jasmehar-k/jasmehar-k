<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 280" width="900" height="280">
  <defs>
    <!-- ═══ Deep space background — desaturated indigo, near-black ═══ -->
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050110"/>
      <stop offset="45%" stop-color="#0d0520"/>
      <stop offset="100%" stop-color="#150a2e"/>
    </linearGradient>

    <!-- Planet sphere — muted violet, lit from upper-left -->
    <radialGradient id="planetGrad" cx="36%" cy="30%" r="72%">
      <stop offset="0%"  stop-color="#b9aee0"/>
      <stop offset="32%" stop-color="#7c6bb8"/>
      <stop offset="68%" stop-color="#4a3585"/>
      <stop offset="100%" stop-color="#241448"/>
    </radialGradient>

    <!-- Day/night terminator shading — the static shadow that sells rotation -->
    <radialGradient id="shade" cx="34%" cy="28%" r="80%">
      <stop offset="0%"  stop-color="#050010" stop-opacity="0"/>
      <stop offset="52%" stop-color="#050010" stop-opacity="0"/>
      <stop offset="78%" stop-color="#0a0318" stop-opacity="0.38"/>
      <stop offset="100%" stop-color="#030008" stop-opacity="0.88"/>
    </radialGradient>

    <!-- Moon sphere -->
    <radialGradient id="moonGrad" cx="35%" cy="32%" r="70%">
      <stop offset="0%" stop-color="#e6e0f5"/>
      <stop offset="55%" stop-color="#9d8fc7"/>
      <stop offset="100%" stop-color="#4a3a78"/>
    </radialGradient>

    <!-- Nebula glows -->
    <radialGradient id="nebula1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#6d5aa8" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#6d5aa8" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="nebula2" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#8b7ac4" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="#8b7ac4" stop-opacity="0"/>
    </radialGradient>

    <!-- Ring gradients — silvery lavender, brightest at the centre of the arc -->
    <linearGradient id="ringMain" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#3d2d70" stop-opacity="0"/>
      <stop offset="16%"  stop-color="#9d8fc7" stop-opacity="0.5"/>
      <stop offset="38%"  stop-color="#cfc4e8" stop-opacity="0.85"/>
      <stop offset="50%"  stop-color="#ece7f8" stop-opacity="1"/>
      <stop offset="62%"  stop-color="#cfc4e8" stop-opacity="0.85"/>
      <stop offset="84%"  stop-color="#9d8fc7" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#3d2d70" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ringOuter" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#4a3585" stop-opacity="0"/>
      <stop offset="28%"  stop-color="#a394d4" stop-opacity="0.35"/>
      <stop offset="50%"  stop-color="#cfc4e8" stop-opacity="0.55"/>
      <stop offset="72%"  stop-color="#a394d4" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#4a3585" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ringInner" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="#6b5a9e" stop-opacity="0"/>
      <stop offset="30%"  stop-color="#d6cbf0" stop-opacity="0.6"/>
      <stop offset="50%"  stop-color="#f3f0fb" stop-opacity="0.9"/>
      <stop offset="70%"  stop-color="#d6cbf0" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#6b5a9e" stop-opacity="0"/>
    </linearGradient>

    <!-- Shooting-star trail -->
    <linearGradient id="trail" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="78" y2="-46">
      <stop offset="0%" stop-color="#ece7f8" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#ece7f8" stop-opacity="0"/>
    </linearGradient>

    <!-- Filters -->
    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="starGlow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <!-- Clips: planet disc + ring halves (evaluated in the tilted local space) -->
    <clipPath id="planetClip"><circle cx="680" cy="130" r="72"/></clipPath>
    <clipPath id="ringBack"><rect x="530" y="130" width="300" height="90"/></clipPath>
    <clipPath id="ringFront"><rect x="530" y="60" width="300" height="70"/></clipPath>
  </defs>

  <!-- ═══ BACKGROUND ═══ -->
  <rect width="900" height="280" fill="url(#bg)"/>
  <ellipse cx="200" cy="80" rx="190" ry="105" fill="url(#nebula1)"/>
  <ellipse cx="650" cy="205" rx="210" ry="120" fill="url(#nebula2)"/>
  <ellipse cx="760" cy="55" rx="150" ry="90" fill="url(#nebula1)"/>
  <ellipse cx="95" cy="225" rx="160" ry="80" fill="url(#nebula2)"/>

  <!-- ═══ STARFIELD ═══ -->
  <!-- Layer 1: distant -->
  <g opacity="0.5">
    <circle cx="12" cy="18" r="0.8" fill="#d6cbf0"><animate attributeName="opacity" values="0.3;1;0.3" dur="3.1s" repeatCount="indefinite"/></circle>
    <circle cx="45" cy="7" r="0.6" fill="#cfc4e8"><animate attributeName="opacity" values="1;0.2;1" dur="2.4s" repeatCount="indefinite"/></circle>
    <circle cx="78" cy="32" r="1" fill="#b4a7d9"><animate attributeName="opacity" values="0.4;1;0.4" dur="4.2s" repeatCount="indefinite"/></circle>
    <circle cx="130" cy="15" r="0.7" fill="#ece7f8"><animate attributeName="opacity" values="0.6;1;0.6" dur="1.9s" repeatCount="indefinite"/></circle>
    <circle cx="160" cy="45" r="0.8" fill="#cfc4e8"><animate attributeName="opacity" values="1;0.3;1" dur="3.7s" repeatCount="indefinite"/></circle>
    <circle cx="205" cy="22" r="0.6" fill="#d6cbf0"><animate attributeName="opacity" values="0.2;1;0.2" dur="2.8s" repeatCount="indefinite"/></circle>
    <circle cx="240" cy="8" r="1.1" fill="#b4a7d9"><animate attributeName="opacity" values="0.7;1;0.7" dur="5.1s" repeatCount="indefinite"/></circle>
    <circle cx="275" cy="38" r="0.5" fill="#cfc4e8"><animate attributeName="opacity" values="1;0.4;1" dur="2.2s" repeatCount="indefinite"/></circle>
    <circle cx="310" cy="12" r="0.9" fill="#ece7f8"><animate attributeName="opacity" values="0.3;1;0.3" dur="3.5s" repeatCount="indefinite"/></circle>
    <circle cx="355" cy="28" r="0.6" fill="#d6cbf0"><animate attributeName="opacity" values="0.8;0.2;0.8" dur="4.8s" repeatCount="indefinite"/></circle>
    <circle cx="390" cy="6" r="0.8" fill="#b4a7d9"><animate attributeName="opacity" values="1;0.5;1" dur="1.7s" repeatCount="indefinite"/></circle>
    <circle cx="430" cy="42" r="0.7" fill="#cfc4e8"><animate attributeName="opacity" values="0.4;1;0.4" dur="3.9s" repeatCount="indefinite"/></circle>
    <circle cx="470" cy="18" r="1" fill="#ece7f8"><animate attributeName="opacity" values="0.6;1;0.6" dur="2.6s" repeatCount="indefinite"/></circle>
    <circle cx="510" cy="9" r="0.6" fill="#d6cbf0"><animate attributeName="opacity" values="1;0.3;1" dur="4.3s" repeatCount="indefinite"/></circle>
    <circle cx="550" cy="35" r="0.9" fill="#b4a7d9"><animate attributeName="opacity" values="0.2;1;0.2" dur="3.1s" repeatCount="indefinite"/></circle>
    <circle cx="590" cy="14" r="0.7" fill="#cfc4e8"><animate attributeName="opacity" values="0.7;0.1;0.7" dur="2.9s" repeatCount="indefinite"/></circle>
    <circle cx="625" cy="44" r="0.5" fill="#ece7f8"><animate attributeName="opacity" values="1;0.6;1" dur="5.4s" repeatCount="indefinite"/></circle>
    <circle cx="820" cy="25" r="0.8" fill="#d6cbf0"><animate attributeName="opacity" values="0.3;1;0.3" dur="3.3s" repeatCount="indefinite"/></circle>
    <circle cx="855" cy="10" r="0.6" fill="#cfc4e8"><animate attributeName="opacity" values="0.8;0.2;0.8" dur="2.1s" repeatCount="indefinite"/></circle>
    <circle cx="885" cy="38" r="1" fill="#b4a7d9"><animate attributeName="opacity" values="1;0.4;1" dur="4.6s" repeatCount="indefinite"/></circle>
  </g>

  <!-- Layer 2: mid-field -->
  <g opacity="0.7">
    <circle cx="28" cy="65" r="1.2" fill="#cfc4e8"><animate attributeName="opacity" values="0.5;1;0.5" dur="2.7s" repeatCount="indefinite"/></circle>
    <circle cx="60" cy="110" r="0.8" fill="#b4a7d9"><animate attributeName="opacity" values="1;0.3;1" dur="3.8s" repeatCount="indefinite"/></circle>
    <circle cx="95" cy="75" r="1.5" fill="#ece7f8"><animate attributeName="opacity" values="0.4;1;0.4" dur="5.2s" repeatCount="indefinite"/></circle>
    <circle cx="140" cy="95" r="0.9" fill="#d6cbf0"><animate attributeName="opacity" values="0.7;0.1;0.7" dur="2.3s" repeatCount="indefinite"/></circle>
    <circle cx="180" cy="130" r="1.1" fill="#cfc4e8"><animate attributeName="opacity" values="1;0.5;1" dur="4.1s" repeatCount="indefinite"/></circle>
    <circle cx="220" cy="85" r="0.7" fill="#b4a7d9"><animate attributeName="opacity" values="0.3;1;0.3" dur="3.4s" repeatCount="indefinite"/></circle>
    <circle cx="260" cy="115" r="1.3" fill="#ece7f8"><animate attributeName="opacity" values="0.6;1;0.6" dur="1.8s" repeatCount="indefinite"/></circle>
    <circle cx="300" cy="70" r="0.8" fill="#d6cbf0"><animate attributeName="opacity" values="1;0.2;1" dur="4.9s" repeatCount="indefinite"/></circle>
    <circle cx="340" cy="100" r="1" fill="#cfc4e8"><animate attributeName="opacity" values="0.4;1;0.4" dur="3.6s" repeatCount="indefinite"/></circle>
    <circle cx="380" cy="80" r="1.4" fill="#b4a7d9"><animate attributeName="opacity" values="0.8;0.3;0.8" dur="2.5s" repeatCount="indefinite"/></circle>
    <circle cx="420" cy="120" r="0.9" fill="#ece7f8"><animate attributeName="opacity" values="1;0.6;1" dur="5.7s" repeatCount="indefinite"/></circle>
    <circle cx="460" cy="65" r="1.1" fill="#d6cbf0"><animate attributeName="opacity" values="0.2;1;0.2" dur="3.2s" repeatCount="indefinite"/></circle>
    <circle cx="500" cy="100" r="0.7" fill="#cfc4e8"><animate attributeName="opacity" values="0.6;0.1;0.6" dur="4.5s" repeatCount="indefinite"/></circle>
    <circle cx="840" cy="80" r="1.2" fill="#b4a7d9"><animate attributeName="opacity" values="0.5;1;0.5" dur="2.9s" repeatCount="indefinite"/></circle>
    <circle cx="870" cy="120" r="0.8" fill="#ece7f8"><animate attributeName="opacity" values="1;0.3;1" dur="4.2s" repeatCount="indefinite"/></circle>
    <circle cx="895" cy="70" r="1" fill="#d6cbf0"><animate attributeName="opacity" values="0.4;1;0.4" dur="3.8s" repeatCount="indefinite"/></circle>
  </g>

  <!-- Layer 3: bright foreground -->
  <g filter="url(#starGlow)">
    <circle cx="55" cy="180" r="1.8" fill="#ece7f8"><animate attributeName="opacity" values="0.6;1;0.6" dur="2.1s" repeatCount="indefinite"/></circle>
    <circle cx="110" cy="220" r="1.5" fill="#cfc4e8"><animate attributeName="opacity" values="1;0.4;1" dur="3.9s" repeatCount="indefinite"/></circle>
    <circle cx="170" cy="195" r="2" fill="#b4a7d9"><animate attributeName="opacity" values="0.3;1;0.3" dur="4.7s" repeatCount="indefinite"/></circle>
    <circle cx="230" cy="240" r="1.3" fill="#ece7f8"><animate attributeName="opacity" values="0.7;0.2;0.7" dur="2.6s" repeatCount="indefinite"/></circle>
    <circle cx="290" cy="210" r="1.6" fill="#cfc4e8"><animate attributeName="opacity" values="1;0.5;1" dur="5.3s" repeatCount="indefinite"/></circle>
    <circle cx="350" cy="250" r="1.2" fill="#d6cbf0"><animate attributeName="opacity" values="0.4;1;0.4" dur="3.1s" repeatCount="indefinite"/></circle>
    <circle cx="410" cy="180" r="1.9" fill="#b4a7d9"><animate attributeName="opacity" values="0.8;0.2;0.8" dur="4.4s" repeatCount="indefinite"/></circle>
    <circle cx="30" cy="250" r="1.4" fill="#cfc4e8"><animate attributeName="opacity" values="0.5;1;0.5" dur="2.8s" repeatCount="indefinite"/></circle>
    <circle cx="860" cy="195" r="1.7" fill="#ece7f8"><animate attributeName="opacity" values="1;0.3;1" dur="3.5s" repeatCount="indefinite"/></circle>
    <circle cx="890" cy="250" r="1.3" fill="#b4a7d9"><animate attributeName="opacity" values="0.4;1;0.4" dur="5.1s" repeatCount="indefinite"/></circle>
  </g>

  <!-- ═══ PIXEL STAR SHAPES ═══ -->
  <g filter="url(#starGlow)">
    <polygon points="90,22 92,27 97,29 92,31 90,36 88,31 83,29 88,27" fill="#cfc4e8" opacity="0.9">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="3.2s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="scale" values="0.8 0.8;1.1 1.1;0.8 0.8" dur="3.2s" repeatCount="indefinite" additive="sum" transform-origin="90 29"/>
    </polygon>
    <polygon points="320,45 321.5,49 325.5,50.5 321.5,52 320,56 318.5,52 314.5,50.5 318.5,49" fill="#b4a7d9" opacity="0.85">
      <animate attributeName="opacity" values="1;0.4;1" dur="4.1s" repeatCount="indefinite"/>
    </polygon>
    <polygon points="500,30 502,36 508,38 502,40 500,46 498,40 492,38 498,36" fill="#ece7f8" opacity="0.95">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2.7s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="rotate" values="0 500 38;15 500 38;0 500 38;-15 500 38;0 500 38" dur="6s" repeatCount="indefinite"/>
    </polygon>
    <polygon points="150,240 151.5,244 155.5,245.5 151.5,247 150,251 148.5,247 144.5,245.5 148.5,244" fill="#9d8fc7" opacity="0.9">
      <animate attributeName="opacity" values="0.6;1;0.6" dur="3.8s" repeatCount="indefinite"/>
    </polygon>
    <polygon points="30,160 32,167 39,169 32,171 30,178 28,171 21,169 28,167" fill="#cfc4e8" opacity="0.8">
      <animate attributeName="opacity" values="1;0.3;1" dur="5s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="scale" values="0.9 0.9;1.15 1.15;0.9 0.9" dur="5s" repeatCount="indefinite" additive="sum" transform-origin="30 169"/>
    </polygon>
    <polygon points="400,255 402,261 408,263 402,265 400,271 398,265 392,263 398,261" fill="#b4a7d9" opacity="0.85">
      <animate attributeName="opacity" values="0.3;1;0.3" dur="4.3s" repeatCount="indefinite"/>
    </polygon>
    <polygon points="875,215 877,221 883,223 877,225 875,231 873,225 867,223 873,221" fill="#ece7f8" opacity="0.8">
      <animate attributeName="opacity" values="1;0.2;1" dur="4.9s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="scale" values="0.85 0.85;1.2 1.2;0.85 0.85" dur="4.9s" repeatCount="indefinite" additive="sum" transform-origin="875 223"/>
    </polygon>
  </g>

  <!-- ═══ DISTANT MINI PLANET (bottom-left flourish) ═══ -->
  <g opacity="0.75">
    <circle cx="475" cy="224" r="5" fill="#6b5a9e"/>
    <circle cx="473.5" cy="222.5" r="2" fill="#9d8fc7" opacity="0.6"/>
    <ellipse cx="475" cy="224" rx="10.5" ry="2.6" fill="none" stroke="#9d8fc7" stroke-width="1" opacity="0.7" transform="rotate(-18 475 224)"/>
    <animate attributeName="opacity" values="0.55;0.85;0.55" dur="6s" repeatCount="indefinite"/>
  </g>

  <!-- ═══ SHOOTING STARS (periodic) ═══ -->
  <g transform="translate(430,18)">
    <g>
      <path d="M0,0 L78,-46" stroke="url(#trail)" stroke-width="1.6" stroke-linecap="round"/>
      <circle cx="0" cy="0" r="1.7" fill="#f3f0fb" filter="url(#starGlow)"/>
      <animateTransform attributeName="transform" type="translate" values="0,0; -300,178; -300,178" keyTimes="0;0.11;1" dur="13s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.95;0;0" keyTimes="0;0.02;0.11;1" dur="13s" repeatCount="indefinite"/>
    </g>
  </g>
  <g transform="translate(890,120)">
    <g>
      <path d="M0,0 L78,-46" stroke="url(#trail)" stroke-width="1.3" stroke-linecap="round"/>
      <circle cx="0" cy="0" r="1.4" fill="#ece7f8" filter="url(#starGlow)"/>
      <animateTransform attributeName="transform" type="translate" values="0,0; -240,142; -240,142" keyTimes="0;0.09;1" dur="19s" begin="-8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.8;0;0" keyTimes="0;0.015;0.09;1" dur="19s" begin="-8s" repeatCount="indefinite"/>
    </g>
  </g>

  <!-- ═══ PLANET SYSTEM — tilted -28°, layered rings, orbiting moon, parallax rotation ═══ -->
  <!-- shift right + scale up, pivoting on the planet centre -->
  <g transform="translate(728,132) scale(1.15) translate(-680,-130)">

  <!-- Breathing halo -->
  <circle cx="680" cy="130" r="92" fill="#6d5aa8" opacity="0.06">
    <animate attributeName="opacity" values="0.04;0.09;0.04" dur="7s" repeatCount="indefinite"/>
  </circle>
  <circle cx="680" cy="130" r="80" fill="#4a3585" opacity="0.1"/>

  <g transform="rotate(-28, 680, 130)">

    <!-- MOON, far side of orbit (behind everything in the system) -->
    <g>
      <circle r="6.5" fill="url(#moonGrad)" opacity="0.75"/>
      <circle r="6.5" fill="#0d0520" opacity="0.3"/>
      <animateMotion path="M530,130 a150,34 0 1,1 300,0 a150,34 0 1,1 -300,0" dur="17s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;1" keyTimes="0;0.5" calcMode="discrete" dur="17s" repeatCount="indefinite"/>
    </g>

    <!-- RING BACK — three bands behind the planet -->
    <g clip-path="url(#ringBack)">
      <ellipse cx="680" cy="130" rx="96"  ry="17" fill="none" stroke="url(#ringInner)" stroke-width="2.5" opacity="0.4"/>
      <ellipse cx="680" cy="130" rx="118" ry="22" fill="none" stroke="url(#ringMain)"  stroke-width="10"  opacity="0.45">
        <animate attributeName="opacity" values="0.4;0.52;0.4" dur="5s" repeatCount="indefinite"/>
      </ellipse>
      <ellipse cx="680" cy="130" rx="134" ry="27" fill="none" stroke="url(#ringOuter)" stroke-width="4"   opacity="0.3"/>
      <!-- ring debris drifting along the far side -->
      <g fill="#cfc4e8" opacity="0.4">
        <circle r="1.2"><animateMotion path="M562,130 a118,22 0 1,1 236,0 a118,22 0 1,1 -236,0" dur="9s"  repeatCount="indefinite"/></circle>
        <circle r="1"><animateMotion path="M562,130 a118,22 0 1,1 236,0 a118,22 0 1,1 -236,0" dur="12s" begin="-4s" repeatCount="indefinite"/></circle>
        <circle r="1.3"><animateMotion path="M584,130 a96,17 0 1,1 192,0 a96,17 0 1,1 -192,0" dur="7s" begin="-2s" repeatCount="indefinite"/></circle>
      </g>
    </g>

    <!-- PLANET BODY -->
    <circle cx="680" cy="130" r="72" fill="url(#planetGrad)" filter="url(#softGlow)"/>

    <!-- ROTATING SURFACE — three parallax layers, each a seamless 144px tile scrolled left -->
    <g clip-path="url(#planetClip)">
      <circle cx="680" cy="130" r="72" fill="#150a2e" opacity="0.15"/>

      <!-- deep bands: slowest -->
      <g opacity="0.9">
        <animateTransform attributeName="transform" type="translate" values="0,0; -144,0" dur="19s" repeatCount="indefinite" calcMode="linear"/>
        <rect x="608" y="72"  width="144" height="12" fill="#2c1a55" opacity="0.5"/>
        <rect x="608" y="96"  width="144" height="15" fill="#1e0f3d" opacity="0.55"/>
        <rect x="608" y="124" width="144" height="17" fill="#241448" opacity="0.5"/>
        <rect x="608" y="152" width="144" height="12" fill="#2c1a55" opacity="0.45"/>
        <rect x="608" y="176" width="144" height="10" fill="#1e0f3d" opacity="0.5"/>
        <rect x="752" y="72"  width="144" height="12" fill="#2c1a55" opacity="0.5"/>
        <rect x="752" y="96"  width="144" height="15" fill="#1e0f3d" opacity="0.55"/>
        <rect x="752" y="124" width="144" height="17" fill="#241448" opacity="0.5"/>
        <rect x="752" y="152" width="144" height="12" fill="#2c1a55" opacity="0.45"/>
        <rect x="752" y="176" width="144" height="10" fill="#1e0f3d" opacity="0.5"/>
      </g>

      <!-- mid bands + great storm: medium speed -->
      <g>
        <animateTransform attributeName="transform" type="translate" values="0,0; -144,0" dur="12s" repeatCount="indefinite" calcMode="linear"/>
        <rect x="608" y="86"  width="144" height="7" fill="#6d5cae" opacity="0.3"/>
        <rect x="608" y="114" width="144" height="8" fill="#5b4a96" opacity="0.32"/>
        <rect x="608" y="144" width="144" height="6" fill="#6d5cae" opacity="0.28"/>
        <rect x="608" y="167" width="144" height="7" fill="#5b4a96" opacity="0.3"/>
        <rect x="752" y="86"  width="144" height="7" fill="#6d5cae" opacity="0.3"/>
        <rect x="752" y="114" width="144" height="8" fill="#5b4a96" opacity="0.32"/>
        <rect x="752" y="144" width="144" height="6" fill="#6d5cae" opacity="0.28"/>
        <rect x="752" y="167" width="144" height="7" fill="#5b4a96" opacity="0.3"/>
        <!-- the great storm, one per tile -->
        <g opacity="0.75">
          <ellipse cx="668" cy="148" rx="16" ry="8.5" fill="#8d7cc4" opacity="0.45"/>
          <ellipse cx="668" cy="148" rx="10" ry="5.5" fill="#a394d4" opacity="0.45"/>
          <ellipse cx="665" cy="146.5" rx="4.5" ry="2.5" fill="#cfc4e8" opacity="0.5"/>
        </g>
        <g opacity="0.75">
          <ellipse cx="812" cy="148" rx="16" ry="8.5" fill="#8d7cc4" opacity="0.45"/>
          <ellipse cx="812" cy="148" rx="10" ry="5.5" fill="#a394d4" opacity="0.45"/>
          <ellipse cx="809" cy="146.5" rx="4.5" ry="2.5" fill="#cfc4e8" opacity="0.5"/>
        </g>
      </g>

      <!-- high wispy clouds: fastest -->
      <g opacity="0.55">
        <animateTransform attributeName="transform" type="translate" values="0,0; -144,0" dur="7.5s" repeatCount="indefinite" calcMode="linear"/>
        <rect x="616" y="80"  width="52" height="3" rx="1.5" fill="#a394d4" opacity="0.5"/>
        <rect x="690" y="103" width="38" height="2.5" rx="1.25" fill="#b4a7d9" opacity="0.45"/>
        <rect x="640" y="133" width="60" height="3" rx="1.5" fill="#a394d4" opacity="0.4"/>
        <rect x="700" y="160" width="34" height="2.5" rx="1.25" fill="#b4a7d9" opacity="0.45"/>
        <rect x="622" y="172" width="44" height="2.5" rx="1.25" fill="#9d8fc7" opacity="0.4"/>
        <rect x="760" y="80"  width="52" height="3" rx="1.5" fill="#a394d4" opacity="0.5"/>
        <rect x="834" y="103" width="38" height="2.5" rx="1.25" fill="#b4a7d9" opacity="0.45"/>
        <rect x="784" y="133" width="60" height="3" rx="1.5" fill="#a394d4" opacity="0.4"/>
        <rect x="844" y="160" width="34" height="2.5" rx="1.25" fill="#b4a7d9" opacity="0.45"/>
        <rect x="766" y="172" width="44" height="2.5" rx="1.25" fill="#9d8fc7" opacity="0.4"/>
      </g>

      <!-- ring shadow cast on the surface -->
      <ellipse cx="680" cy="134" rx="72" ry="7" fill="#030008" opacity="0.32"/>

      <!-- static day/night terminator + specular — the fixed light that makes the scroll read as rotation -->
      <circle cx="680" cy="130" r="72" fill="url(#shade)"/>
      <ellipse cx="652" cy="102" rx="26" ry="16" fill="#e6e0f5" opacity="0.16"/>
      <ellipse cx="645" cy="97"  rx="12" ry="7"  fill="#ffffff" opacity="0.08"/>
    </g>

    <!-- atmosphere rim -->
    <circle cx="680" cy="130" r="72.5" fill="none" stroke="#b4a7d9" stroke-width="1.2" opacity="0.28" filter="url(#starGlow)"/>

    <!-- RING FRONT — three bands crossing the planet -->
    <g clip-path="url(#ringFront)">
      <ellipse cx="680" cy="130" rx="96"  ry="17" fill="none" stroke="url(#ringInner)" stroke-width="2.5" opacity="0.75"/>
      <ellipse cx="680" cy="130" rx="118" ry="22" fill="none" stroke="url(#ringMain)"  stroke-width="10"  opacity="0.8">
        <animate attributeName="opacity" values="0.72;0.9;0.72" dur="5s" repeatCount="indefinite"/>
      </ellipse>
      <ellipse cx="680" cy="130" rx="134" ry="27" fill="none" stroke="url(#ringOuter)" stroke-width="4"   opacity="0.55"/>
      <!-- ring debris sweeping across the near side -->
      <g fill="#ece7f8" opacity="0.9" filter="url(#starGlow)">
        <circle r="1.2"><animateMotion path="M562,130 a118,22 0 1,1 236,0 a118,22 0 1,1 -236,0" dur="9s"  repeatCount="indefinite"/></circle>
        <circle r="1"><animateMotion path="M562,130 a118,22 0 1,1 236,0 a118,22 0 1,1 -236,0" dur="12s" begin="-4s" repeatCount="indefinite"/></circle>
        <circle r="1.3"><animateMotion path="M584,130 a96,17 0 1,1 192,0 a96,17 0 1,1 -192,0" dur="7s" begin="-2s" repeatCount="indefinite"/></circle>
      </g>
    </g>

    <!-- MOON, near side of orbit (in front of everything) -->
    <g>
      <circle r="8" fill="url(#moonGrad)"/>
      <circle cx="-2.5" cy="1.5" r="1.6" fill="#4a3a78" opacity="0.5"/>
      <circle cx="3" cy="-2" r="1.1" fill="#4a3a78" opacity="0.4"/>
      <circle cx="1.5" cy="4" r="0.9" fill="#4a3a78" opacity="0.35"/>
      <animateMotion path="M530,130 a150,34 0 1,1 300,0 a150,34 0 1,1 -300,0" dur="17s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0" keyTimes="0;0.5" calcMode="discrete" dur="17s" repeatCount="indefinite"/>
    </g>

  </g>
  </g>
  <!-- ── end tilted group ── -->

  <!-- ═══ TEXT ═══ -->
  <text x="80" y="110" font-family="'Courier New', monospace" font-size="42" font-weight="bold" fill="#d6cbf0" filter="url(#glow)" letter-spacing="3">Jasmehar Kaur</text>
  <text x="82" y="145" font-family="'Courier New', monospace" font-size="13" fill="#9d8fc7" letter-spacing="2" opacity="0.9">✦ code · build · iterate ✦</text>
  <text x="82" y="185" font-family="'Courier New', monospace" font-size="11" fill="#6b5a9e" letter-spacing="1.5" opacity="0.85">working on a better version of myself, one patch at a time</text>

  <circle cx="67" cy="108" r="2.5" fill="#6b5a9e" opacity="0.7"/>
  <circle cx="67" cy="143" r="1.5" fill="#9d8fc7" opacity="0.6"/>

  <text x="0" y="272" font-family="'Courier New', monospace" font-size="9" fill="#3d2d70" letter-spacing="8" opacity="0.75">· · ✦ · · · · ✦ · · · · ✦ · · · · ✦ · · · · ✦ · · · · ✦ · · · · ✦ · · · · ✦ · · · · ✦ · · · · ✦ · ·</text>
</svg>
