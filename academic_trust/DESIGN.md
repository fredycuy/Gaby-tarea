---
name: Academic Trust
colors:
  surface: '#f8f9ff'
  surface-dim: '#d0dbed'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e6eeff'
  surface-container-high: '#dee9fc'
  surface-container-highest: '#d9e3f6'
  on-surface: '#121c2a'
  on-surface-variant: '#3f4940'
  inverse-surface: '#27313f'
  inverse-on-surface: '#eaf1ff'
  outline: '#6f7a70'
  outline-variant: '#bec9be'
  surface-tint: '#0b6d3b'
  primary: '#004d27'
  on-primary: '#ffffff'
  primary-container: '#006837'
  on-primary-container: '#8ee4a6'
  inverse-primary: '#83d99c'
  secondary: '#666000'
  on-secondary: '#ffffff'
  secondary-container: '#f0e427'
  on-secondary-container: '#6a6500'
  tertiary: '#1a4377'
  on-tertiary: '#ffffff'
  tertiary-container: '#365b90'
  on-tertiary-container: '#bbd3ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#9ef6b6'
  primary-fixed-dim: '#83d99c'
  on-primary-fixed: '#00210e'
  on-primary-fixed-variant: '#00522a'
  secondary-fixed: '#f3e72b'
  secondary-fixed-dim: '#d6ca00'
  on-secondary-fixed: '#1e1c00'
  on-secondary-fixed-variant: '#4d4800'
  tertiary-fixed: '#d5e3ff'
  tertiary-fixed-dim: '#a7c8ff'
  on-tertiary-fixed: '#001b3c'
  on-tertiary-fixed-variant: '#1f477b'
  background: '#f8f9ff'
  on-background: '#121c2a'
  surface-variant: '#d9e3f6'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style
The brand personality for the design system is authoritative yet accessible, bridging the gap between traditional academic prestige and modern financial utility. It is designed for students and faculty of the Universidad Técnica de Babahoyo (UTB) who require clarity, speed, and reliability when managing educational credits.

The design style is **Corporate / Modern** with a focus on high-density information architecture. It prioritizes legibility and structure, using a refined grid system and subtle depth to guide the user through complex financial data. The aesthetic balances the institutional weight of the university with the frictionless experience expected of contemporary fintech platforms.

## Colors
The palette is derived from the official UTB identity, reinforced with deep navy tones for financial credibility.

- **Primary (Emerald Green):** Used for main actions, active states, and brand-heavy components. It represents growth and institutional identity.
- **Secondary (Golden Yellow):** Used sparingly as a highlight color for high-visibility alerts, notification badges, or subtle accents to draw attention without overpowering the content.
- **Tertiary (Institutional Blue):** Employed for structural elements, headers, and secondary navigation to ground the UI in a professional, banking-oriented context.
- **Surface & Neutrals:** A clean white background with varied grays for borders and secondary text ensures a high-contrast, accessible reading environment.

## Typography
This design system utilizes **Inter** exclusively to achieve a systematic and utilitarian feel. The hierarchy relies on substantial weight differences (Bold vs. Regular) to establish clear information scaffolding.

- **Headlines:** Use Bold (700) weights with tighter letter-spacing for a modern, impactful look.
- **Body:** Set with generous line-heights to maintain readability during long-form reading of terms and conditions or loan details.
- **Labels:** Uppercase styles may be applied to `label-sm` for category tags or metadata to differentiate them from body copy.

## Layout & Spacing
The layout follows a **Fluid Grid** model with fixed maximum widths for desktop viewing to prevent line lengths from becoming unreadable.

- **Desktop (1440px+):** 12-column grid with 24px gutters and 64px outside margins.
- **Tablet (768px - 1439px):** 8-column grid with 24px gutters and 32px margins.
- **Mobile (Up to 767px):** 4-column grid with 16px gutters and 16px margins.

Spacing follows a strict 4px/8px incremental scale. Vertical rhythm is maintained by using the `lg` (24px) unit for spacing between major sections and `md` (16px) for internal component padding.

## Elevation & Depth
The design system uses **Tonal Layers** and soft **Ambient Shadows** to define hierarchy.

- **Level 0 (Surface):** The base background, typically white (#FFFFFF) or very light gray (#F9FAFB).
- **Level 1 (Cards):** Low-contrast outlines (1px border in #E5E7EB) with a very soft, diffused shadow (0px 4px 12px rgba(0, 0, 0, 0.05)).
- **Level 2 (Modals/Overlays):** Higher contrast shadows (0px 12px 24px rgba(0, 51, 102, 0.1)) to pull elements forward.

Interactive elements like buttons should feel "pressed" on active states by removing the shadow, while hovering should slightly increase the shadow's spread.

## Shapes
The shape language is **Soft**, utilizing a 4px (0.25rem) base radius. This conservative rounding maintains a professional and stable appearance suitable for a financial institution while feeling more approachable than sharp, 0px corners.

- **Buttons & Inputs:** 4px radius.
- **Cards & Containers:** 8px (rounded-lg) to provide a clear container-level distinction.
- **Modals:** 12px (rounded-xl) for a softer, prominent look.

## Components
- **Buttons:** Primary buttons use Emerald Green (#006837) with white text. Secondary buttons use Institutional Blue (#003366) as an outline or ghost style. The Golden Yellow is reserved for "Warning" or "Alert" buttons.
- **Input Fields:** Use a 1px border (#D1D5DB) that shifts to Primary Green on focus. Labels are always visible above the field in `label-md` weight.
- **Cards:** White backgrounds with a subtle border and Level 1 elevation. Header sections within cards may use a light Institutional Blue tint (#F0F4F8) to group metadata.
- **Chips/Status Tags:** Use high-saturation, low-opacity backgrounds (e.g., Green tint for 'Approved', Blue tint for 'Pending') with dark text of the same hue for maximum accessibility.
- **Lists:** Data-heavy lists should use alternating row backgrounds (Zebra striping) or subtle dividers to ensure horizontal tracking remains accurate across wide screens.