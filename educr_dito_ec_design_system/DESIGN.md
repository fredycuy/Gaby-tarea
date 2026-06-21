---
name: EduCrédito EC Design System
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#43474f'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#737780'
  outline-variant: '#c3c6d1'
  surface-tint: '#3a5f94'
  primary: '#001e40'
  on-primary: '#ffffff'
  primary-container: '#003366'
  on-primary-container: '#799dd6'
  inverse-primary: '#a7c8ff'
  secondary: '#1b6d24'
  on-secondary: '#ffffff'
  secondary-container: '#a0f399'
  on-secondary-container: '#217128'
  tertiary: '#16211a'
  on-tertiary: '#ffffff'
  tertiary-container: '#2b362e'
  on-tertiary-container: '#929f94'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e3ff'
  primary-fixed-dim: '#a7c8ff'
  on-primary-fixed: '#001b3c'
  on-primary-fixed-variant: '#1f477b'
  secondary-fixed: '#a3f69c'
  secondary-fixed-dim: '#88d982'
  on-secondary-fixed: '#002204'
  on-secondary-fixed-variant: '#005312'
  tertiary-fixed: '#d9e6da'
  tertiary-fixed-dim: '#bdcabe'
  on-tertiary-fixed: '#131e17'
  on-tertiary-fixed-variant: '#3e4a41'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
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
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  title-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
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
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: auto
  max-width: 1200px
---

## Brand & Style
The design system is built upon a foundation of **Corporate Modernism** infused with **Minimalist** clarity. The objective is to bridge the gap between institutional authority and student accessibility. Given the target audience of university students, the interface must project absolute security and financial literacy without appearing intimidating or overly bureaucratic.

The aesthetic emphasizes high legibility, generous whitespace to reduce cognitive load during complex financial tasks, and a "Safety-First" visual hierarchy. It avoids unnecessary flourishes, focusing instead on structural integrity and functional elegance to foster a sense of reliability and progress.

## Colors
The palette is rooted in a deep **Institutional Blue (#003366)**, serving as the primary anchor for headers, primary actions, and branding elements to evoke trust and stability. 

To balance the weight of the blue, a **Soft Green (#E8F5E9)** is utilized as a secondary surface color for success states, background containers, and highlight areas, symbolizing growth and financial health. For high-priority interactive elements like "Apply" or "Confirm," a more saturated **Forest Green (#2E7D32)** is employed to ensure AA accessibility standards are met against white backgrounds. Neutrals are kept cool-toned to maintain a professional and clean environment.

## Typography
This design system utilizes **Inter** exclusively to ensure a systematic and utilitarian feel across all platforms. Inter's tall x-height and excellent legibility at small sizes make it ideal for data-heavy micro-credit applications and complex forms.

Headlines use a semi-bold weight with tight letter-spacing to create a strong visual impact and "anchored" feeling. Body text maintains a standard weight for maximum readability. Labels and captions use a medium weight to differentiate them from static body copy, ensuring students can quickly scan through loan terms and requirements.

## Layout & Spacing
The layout follows a **Fixed-Grid** philosophy for desktop to maintain a contained, professional appearance, while transitioning to a **Fluid-Grid** for mobile devices to accommodate the high traffic from student smartphones.

- **Desktop:** 12-column grid, 1200px max-width, 24px gutters.
- **Tablet:** 8-column grid, 24px margins.
- **Mobile:** 4-column grid, 16px margins.

Spacing follows a strict 8pt rhythm (using a 4px base unit) to ensure mathematical harmony between components. Vertical rhythm is prioritized in forms to group related input fields logically, using larger gaps (`lg`) to separate distinct sections of a loan application.

## Elevation & Depth
To convey security and modernity, the design system utilizes **Tonal Layers** combined with **Ambient Shadows**. Instead of harsh borders, depth is created through subtle shifts in background color and very soft, diffused shadows.

- **Level 0 (Surface):** The main background uses `#FFFFFF`.
- **Level 1 (Cards/Inputs):** Elements sit on the surface with a very soft shadow (0px 4px 20px rgba(0, 51, 102, 0.05)).
- **Level 2 (Active/Hover):** Interactive elements or focused cards lift slightly with a more pronounced shadow (0px 8px 30px rgba(0, 51, 102, 0.08)).
- **Level 3 (Modals):** High-elevation components use a backdrop blur of 8px to maintain focus on the task at hand.

## Shapes
The shape language is consistently **Rounded**, reflecting a friendly and approachable personality. Standard UI components like buttons and input fields use a `0.5rem` (8px) radius. 

Larger containers, such as credit summary cards or application progress modules, utilize `rounded-lg` (16px) or `rounded-xl` (24px) to create a distinct, modern "app-like" feel that differentiates the platform from traditional, sharp-edged banking software. This softer geometry helps reduce the perceived stress associated with financial borrowing.

## Components

### Buttons
Primary action buttons use the Institutional Blue with white text, utilizing a bold weight for the label. Secondary buttons use a transparent background with a 1.5px blue border. "Apply" or "Success" buttons may use the Forest Green variant. All buttons have a height of 48px to ensure a comfortable tap target for mobile users.

### Cards
Credit cards and info-modules must use a white background with a 1px border in a very light neutral (`#E2E8F0`) and the Level 1 shadow. They should include a 24px internal padding to ensure content has room to breathe.

### Interactive Simulators
Loan calculators use "Soft Green" (`#E8F5E9`) for the container background. Range sliders should be thick and easy to manipulate, using the primary blue for the active track and a large white thumb with a shadow.

### Form Inputs & Validation
Inputs must have a 1px neutral border that turns into a 2px blue border on focus. 
- **Error State:** Border becomes `#DC2626` with a small error icon and caption text below.
- **Success State:** Border becomes `#16A34A` once the specific field validation (e.g., UTB ID format) is passed.

### Progress Indicators
For multi-step applications, use a horizontal stepper on desktop and a "Step X of Y" label with a thin progress bar on mobile, positioned at the top of the viewport.