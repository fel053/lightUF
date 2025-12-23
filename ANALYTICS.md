# Vercel Web Analytics Integration

This project has been integrated with Vercel Web Analytics to track visitor behavior and page performance.

## Overview

Vercel Web Analytics is a lightweight Web Vitals monitoring and analytics platform that helps you understand how your users experience your site.

## How It Works

The analytics script is automatically injected into all generated HTML pages through the templates:
- `templates/uf_static.html` - The main converter pages
- `templates/uf_human.html` - The human-readable calculator page

## Implementation Details

### Script Injection

The following code is added to the `<body>` section of each HTML template:

```html
<!-- Vercel Web Analytics -->
<script>
  window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
</script>
<script defer src="/_vercel/insights/script.js"></script>
```

This script:
1. Initializes the analytics queue if not already present
2. Loads the Vercel insights script asynchronously
3. Tracks page views and Web Vitals metrics automatically

### Deployment Requirements

To enable Web Analytics tracking:

1. **Enable in Vercel Dashboard**
   - Navigate to your project's Analytics tab
   - Click "Enable" to activate Web Analytics
   - This creates the necessary `/_vercel/insights/*` routes

2. **Deploy to Vercel**
   - Use `vercel deploy` or push to your connected Git repository
   - The build script (`build.py`) will generate all HTML pages with analytics included

3. **View Data**
   - After deployment and initial visitors, visit your project's Analytics tab
   - Data will start appearing within a few minutes

## Data Collection

The analytics script automatically collects:
- Page views and route information
- Web Vitals (LCP, CLS, FID, TTFB)
- Browser and device information
- Performance metrics

## Privacy

Vercel Web Analytics is designed with privacy in mind:
- No cookies are set
- IP addresses are anonymized
- Compliant with privacy regulations (GDPR, CCPA, etc.)

## Build Process

The build script (`build.py`) generates static HTML pages from templates. All generated pages will include the analytics script automatically through template substitution.

Example build command:
```bash
python3 build.py
```

This generates:
- Static pages in the `output/` directory
- Each page for a specific UF value under `output/uf/{value}/`
- All pages include the Vercel Web Analytics script

## Troubleshooting

If analytics data is not appearing:

1. Verify Web Analytics is enabled in the Vercel dashboard
2. Check the browser's Network tab for requests to `/_vercel/insights/script.js` and `/_vercel/insights/view`
3. Ensure the site is deployed to Vercel (analytics won't work locally)
4. Wait a few minutes for data to appear after initial deployment

## Further Reading

- [Vercel Web Analytics Documentation](https://vercel.com/docs/analytics)
- [Web Vitals Guide](https://web.dev/vitals/)
- [Privacy & Compliance](https://vercel.com/docs/analytics/privacy-policy)
