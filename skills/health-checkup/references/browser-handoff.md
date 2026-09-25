# Browser capability ladder and semantic takeover

SPDX-License-Identifier: CC-BY-4.0

Use the safest available level, not the most autonomous one. Do not install extensions, change browser security settings, or seek a bypass.

| Level | Action | Checkpoint |
|---|---|---|
| Site-native API/plugin | Read official public offerings via available documented tool | No unofficial endpoint probing, credentials or external writes without consent |
| Browser | Inspect actual page, labels, state and destination; fill only consented safe fields | Check autosave and whether “next” sends data |
| Browser + takeover | Pause at CAPTCHA/OTP/passkey/payment verification; user completes privately | Resume only after user reports completion; inspect new page and session validity |
| Local browser handoff | Give canonical URL, branch/package, current step and restart instructions | Remote cookies/filled values may not transfer; say so; do not export them |
| Guided manual | User opens page; agent translates redacted screenshots/text, one field at a time | Explain missing context rather than guess; user does final submission |

A local browser handoff is often followed by manual guidance. If tooling is unavailable, it is a normal successful fallback, not a reason to abandon assistance.

## Handoff packet

Provide: official URL/domain; expected page title; selected branch/package; progress and unsaved work; exact human checkpoint; Japanese control label plus procedural English; what happens on click; sensitive data that should be entered privately; next safe point to return; what success looks like. User may crop identifiers out of screenshots. Never request OTP, password or CAPTCHA solution in chat. Do not claim that an automation block has been bypassed.

## Translation contract

Prefer side-by-side explanation, keeping the underlying page untouched. Browser-native translation is optional only if it does not break controls; revert if it does. An overlay/extension can be a future adapter but is not implemented or required. Explain labels, dropdown choices, format examples, validation errors, warnings and final confirmation screens. Preserve negation, units, deadlines, required markers and consequential distinctions. Repeat exact Japanese so the user can locate the control; do not invent selectors.

| Japanese | Procedural English |
|---|---|
| 受診票 | Health-check form/questionnaire; inspect issuer instructions to see whether to complete it beforehand and bring it. Not necessarily the subsidy voucher. |
| 受診券 | Eligibility/visit voucher. Check program, valid period and designated providers; bring as instructed. |
| 保険証番号 / 記号・番号 | Insurance identifier fields: match the requested label on eligibility documentation. Do not substitute My Number; ask provider if unclear. |
| 氏名（フリガナ） | Name reading, usually katakana; follow the page's full-/half-width instructions, not an invented romanization. |
| 必須 / 任意 | Required / optional; optional is not necessary consent. |
| 確認画面へ | Go to review; may still transmit draft values, so sensitive-entry consent comes first. |
| 予約を確定する | Finalize reservation: stop for explicit approval after reviewing package, time, amount and terms. |
| 送信 / キャンセル | Send / cancel; distinguish canceling this screen from canceling an existing booking using context. |
| 入力内容に誤りがあります | There is an input error; inspect highlighted field and required format rather than resubmitting blindly. |

Example: “Click **確認画面へ** only after checking the data shown. This should lead to review, not prove a booking. On the next page, look for **予約を確定する**. Please pause there so we can review consequences. Enter your authentication code privately; do not send it to me.”

## Resume and outcome

After takeover check whether a booking was submitted already. Record only administrative status in the session; do not duplicate a booking. Read confirmation number privately if needed, date/time JST, location, package, payment/cancellation terms, preparation and result delivery. If there is no receipt and status is uncertain, help the user verify with the provider instead of retrying.
