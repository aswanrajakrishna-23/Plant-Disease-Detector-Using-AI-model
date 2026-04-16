# Design System Strategy: The Botanical Editorial

## 1. Overview & Creative North Star
The "Botanical Editorial" is the creative North Star of this design system. We are moving away from the cold, clinical nature of traditional diagnostic tools and toward a high-end, scientific journal aesthetic. The goal is to make the user feel like a modern botanist. 

We break the "standard app" mold by prioritizing **intentional asymmetry** and **tonal depth**. Instead of rigid grids, we use overlapping elements—such as a high-quality plant image bleeding off the edge of a `surface-container`—to create a sense of organic growth. This system balances the precision of data-driven diagnosis with the soft, tactile feel of a premium lifestyle magazine.

## 2. Colors: Tonal Atmosphere
Our palette is rooted in the natural world, utilizing deep forest greens and sun-bleached earth tones to establish authority and calm.

### The "No-Line" Rule
**Strict Mandate:** Designers are prohibited from using 1px solid borders to define sections. Layout boundaries must be achieved through:
- **Color Shifts:** Use `surface-container-low` for secondary content sitting atop a `background` or `surface` base.
- **Negative Space:** Use the Spacing Scale (specifically `8` [2.75rem] and `10` [3.5rem]) to create natural visual breaks.

### Surface Hierarchy & Nesting
Think of the UI as layers of fine vellum paper. 
- Use `surface-container-lowest` (#ffffff) for floating high-priority cards.
- Use `surface-container-high` (#e7e8e7) for recessed utility areas like search bars or navigation docks.
- This creates "nested depth" where the eye follows color transitions rather than lines.

### The "Glass & Gradient" Rule
To elevate the "Modern" feel, use **Glassmorphism** for floating action buttons or diagnostic overlays. Apply `surface` with a 70% opacity and a 20px backdrop-blur. 
- **Signature Texture:** For primary CTAs (like "Start Diagnosis"), use a subtle linear gradient transitioning from `primary` (#204e2b) to `primary_container` (#386641) at a 135-degree angle. This adds "soul" and dimension that flat colors cannot mimic.

## 3. Typography: The Curated Voice
We utilize a pairing of **Manrope** (Display/Headline) and **Inter** (Title/Body) to bridge the gap between "Professional" and "Approachable."

- **Manrope (Display & Headline):** Used for impactful moments—plant names, health scores, and hero titles. Its geometric yet soft curves feel modern and high-end.
- **Inter (Title & Body):** Used for technical data and diagnostic instructions. It provides maximum legibility for dense botanical information.
- **Visual Hierarchy:** Use `display-lg` (3.5rem) for health percentages, set in `on_surface` (#191c1c). Pair this with `label-md` in `on_secondary_container` (#775e3c) to provide earthy contrast and clear data attribution.

## 4. Elevation & Depth: Atmospheric Layering
Traditional drop shadows are too heavy for this botanical aesthetic. We use **Tonal Layering** to define the Z-axis.

- **The Layering Principle:** To lift a diagnostic card, place a `surface-container-lowest` card on a `surface-container-low` background. The subtle shift in hex code provides all the "lift" needed.
- **Ambient Shadows:** If a card must float over a high-quality image, use a shadow with a blur of `32px`, an Y-offset of `8px`, and a color of `on_surface` at **4% opacity**. It should feel like a soft glow, not a shadow.
- **The "Ghost Border" Fallback:** If accessibility requires a stroke, use the `outline_variant` (#c1c9be) at **15% opacity**. Anything higher is too aggressive for this system.

## 5. Components: Botanical Primitives

### Cards & Lists (The Editorial Feed)
- **Rules:** Forbid all divider lines.
- **Execution:** Separate plant items in a list using a `2.5` (0.85rem) vertical gap. Use a `surface-container` background for the entire list block to unify it against the `surface` background.
- **Imagery:** Cards should feature high-quality botanical imagery with a corner radius of `lg` (1rem).

### Buttons (Tactile Interactions)
- **Primary:** Gradient-filled (`primary` to `primary_container`), `full` roundedness (9999px), using `title-sm` typography.
- **Secondary:** `surface_container_high` background with `on_surface_variant` text. No border.
- **Tertiary:** Text-only in `primary`, used for "Learn More" links.

### Diagnostic Input Fields
- **Styling:** Use a `surface_container_low` fill with a `md` (0.75rem) radius. 
- **Active State:** On focus, transition the background to `surface_container_lowest` and add a "Ghost Border" of `primary` at 20% opacity.

### Signature Component: The Health Spectrum
- A horizontal gauge using a gradient from `error` (#ba1a1a) to `primary` (#204e2b). Use a floating `surface-container-lowest` indicator to mark the plant's current health status.

## 6. Do's and Don'ts

### Do
- **Do** allow plant imagery to overlap text containers to create a "layered" editorial look.
- **Do** use the `secondary` (#725a38) and `tertiary` (#244e0b) tokens for labels—this keeps the app feeling "earthy" rather than "techy."
- **Do** use generous whitespace. If in doubt, increase the spacing by one level on the scale.

### Don't
- **Don't** use 100% black (#000000). Use `on_surface` (#191c1c) for all "black" text.
- **Don't** use sharp corners. Every container must have at least a `DEFAULT` (0.5rem) radius to maintain the "Organic" feel.
- **Don't** use standard "Success Green." Use the system's `primary` (#204e2b) which is a sophisticated, natural forest green.