# YouTube API audit — submission record

**Submitted:** 28 October 2026, 12:0x EDT (Google confirmed: "Your email has been sent — Thank you for submitting the YouTube API Services Form.")
**Form:** YouTube Data API Services — Audit and Quota Extension Form.

## What was submitted

| field | value |
|---|---|
| Request type | Compliance audit **to request additional quota** |
| Applicant | Individual — Kai Ronen (legal name supplied privately by the owner) |
| Organisation | `self` |
| Category | Creator Tools and Services |
| API client | Reelwright (does not contain the word "YouTube") |
| Primary access URL | https://youraveragecow.github.io/reelwright-site/ |
| Privacy policy | https://youraveragecow.github.io/reelwright-site/privacy.html |
| Terms | https://youraveragecow.github.io/reelwright-site/terms.html |
| Publicly accessible | No (local desktop app) |
| Project | 984445733063 / `reelwright-513015` |
| Use case | Video Uploading & Account Management; Tools for Creators |
| OAuth | Yes |
| Expected volume | Fewer than 1,000 requests/day |
| Endpoint | `youtube.videos.insert` only |
| **Quota requested** | **160,000 units/day total; 100 `videos.insert` calls/day** (100 × 1,600 units) |

## Evidence attached

- Architecture diagram — `evidence/architecture.png`
- User-flow diagram — `evidence/user-flow.png`
- Privacy policy screenshot — `evidence/shot-privacy.png`
- Homepage screenshot showing the privacy link — `evidence/shot-home-links.png`
- Terms screenshot — `evidence/shot-terms.png`
- OAuth flow (4 screens: account, brand channel, unverified warning, consent) — `evidence/oauth-flow.pdf`
- Upload implementation + live evidence — `evidence/upload-script.pdf`
- End-to-end screencast — https://youraveragecow.github.io/reelwright-site/evidence/upload-flow.html

## Uploads proven before submission

| video | URL | note |
|---|---|---|
| Stolen Parking Spot | https://youtu.be/SD4PneZtVh4 | first live upload |
| The Letter Dated Tomorrow | https://youtu.be/K9gRiLPjIzQ | recorded run |
| (batch test) | https://youtu.be/nHDHOAyUIfc | recorded run |
| (screencast run) | https://youtu.be/b2V6PoddiAI | the run shown in the screencast |

All are **private**: YouTube forces private visibility for API clients that have not completed this audit. That is the restriction this submission exists to lift.

## What happens next

1. Google reviews (days to weeks). Expect at least one round of questions; the common asks are a clearer screencast or a narrower quota justification.
2. If the audit passes: uploads can be public, and the quota increase may be granted in part (100/day is a large step from the default 6).
3. The OAuth consent screen is already published to production, so refresh tokens no longer expire every 7 days. Verification (removing the "unverified app" interstitial) is a *separate* review and was not requested here; it does not affect this single-user app's ability to upload.
