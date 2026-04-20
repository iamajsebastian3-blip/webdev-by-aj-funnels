"""Builds the 'Your Business, On Autopilot.' lead magnet PDF with WEBDEV BY AJ branding."""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
import os

OUT = os.path.join(os.path.dirname(__file__), "business-on-autopilot.pdf")

PURPLE = HexColor("#5E17EB")
PURPLE_BRIGHT = HexColor("#7B3FFF")
YELLOW = HexColor("#FFD600")
DARK = HexColor("#0A0A0A")
GRAY = HexColor("#5A5A5A")
LIGHT_GRAY = HexColor("#E8E8E8")
BG_SOFT = HexColor("#FAFAFA")
PAIN_BG = HexColor("#FFF7E6")

W, H = LETTER
MARGIN_L = 60
MARGIN_R = 60

CONSULTATION_URL = "ajautomate.co/consultation"


def wrap_text(c, text, font, size, max_width):
    c.setFont(font, size)
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if c.stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(c, text, x, y, font, size, max_width, leading, color=DARK):
    c.setFillColor(color)
    lines = wrap_text(c, text, font, size, max_width)
    for line in lines:
        c.setFont(font, size)
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_brand_footer(c, page_num=None, total=None):
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(GRAY)
    c.drawString(MARGIN_L, 30, "WEBDEV BY ")
    c.setFillColor(YELLOW)
    c.drawString(MARGIN_L + c.stringWidth("WEBDEV BY ", "Helvetica-Bold", 8), 30, "AJ")
    c.setFillColor(GRAY)
    tail = "  —  Premium Websites & Funnels"
    c.drawString(MARGIN_L + c.stringWidth("WEBDEV BY AJ", "Helvetica-Bold", 8), 30, tail)
    if page_num and total:
        c.setFont("Helvetica", 8)
        c.setFillColor(GRAY)
        page_str = f"{page_num} / {total}"
        c.drawRightString(W - MARGIN_R, 30, page_str)


def page_cover(c):
    c.setFillColor(PURPLE)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    c.setFillColor(YELLOW)
    c.rect(MARGIN_L, H - 120, 60, 6, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(YELLOW)
    c.drawString(MARGIN_L, H - 150, "FREE GUIDE  ·  WEBDEV BY AJ")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 44)
    c.drawString(MARGIN_L, H - 220, "Your Business,")
    c.setFillColor(YELLOW)
    c.drawString(MARGIN_L, H - 270, "On Autopilot.")

    c.setFillColor(white)
    sub = ("How a website, automated messenger, and AI assistant can handle "
           "your inquiries — so you can grow your business, not just reply to it.")
    y = H - 325
    lines = wrap_text(c, sub, "Helvetica", 13, W - MARGIN_L - MARGIN_R - 40)
    for line in lines:
        c.setFont("Helvetica", 13)
        c.drawString(MARGIN_L, y, line)
        y -= 20

    # Generous spacing before callout
    y -= 40

    # Feature callout (vertical yellow accent bar + text)
    c.setFillColor(YELLOW)
    c.rect(MARGIN_L, y - 30, 4, 48, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(white)
    c.drawString(MARGIN_L + 18, y + 4, "Built for local businesses tired of answering the")
    c.drawString(MARGIN_L + 18, y - 14, "same customer questions over and over again.")

    # Divider
    c.setStrokeColor(YELLOW)
    c.setLineWidth(2)
    c.line(MARGIN_L, 140, MARGIN_L + 80, 140)

    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(white)
    c.drawString(MARGIN_L, 110, "WEBDEV BY ")
    c.setFillColor(YELLOW)
    c.drawString(MARGIN_L + c.stringWidth("WEBDEV BY ", "Helvetica-Bold", 11), 110, "AJ")
    c.setFillColor(white)
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN_L, 92, "Premium Websites & Funnels  ·  Built to convert")

    c.showPage()


def page_intro(c, page_num, total):
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    c.setFillColor(PURPLE)
    c.rect(0, H - 8, W, 8, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(PURPLE)
    c.drawString(MARGIN_L, H - 70, "THE PROBLEM")

    c.setFont("Helvetica-Bold", 32)
    c.setFillColor(DARK)
    c.drawString(MARGIN_L, H - 115, "Does this sound like you?")

    c.setFillColor(YELLOW)
    c.rect(MARGIN_L, H - 125, 120, 4, fill=1, stroke=0)

    body_width = W - MARGIN_L - MARGIN_R
    pain_points = [
        "You answer the same 5 questions on Messenger all day long.",
        "You reply to customer DMs at 11pm because you can't miss a booking.",
        "You lose customers because you can't reply fast enough during busy hours.",
        "You can't take a real day off — the business stops the moment you do.",
        "You want to grow, but there's no time left to plan, market, or scale.",
    ]

    y = H - 170
    for point in pain_points:
        # Red-ish X mark circle
        c.setFillColor(HexColor("#FFE4E4"))
        c.circle(MARGIN_L + 12, y + 4, 10, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(HexColor("#D93A3A"))
        c.drawCentredString(MARGIN_L + 12, y + 1, "✕")

        # Pain text
        text_x = MARGIN_L + 34
        text_w = body_width - 34
        lines = wrap_text(c, point, "Helvetica", 12, text_w)
        line_y = y + 4
        c.setFillColor(DARK)
        for line in lines:
            c.setFont("Helvetica", 12)
            c.drawString(text_x, line_y, line)
            line_y -= 16
        y -= 36 if len(lines) == 1 else 52

    y -= 10

    # Yellow callout box
    c.setFillColor(PAIN_BG)
    callout_h = 70
    c.roundRect(MARGIN_L, y - callout_h, body_width, callout_h, 10, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(DARK)
    c.drawString(MARGIN_L + 20, y - 24, "Here's what's possible when you put the right systems in place:")

    c.setFont("Helvetica", 11)
    c.setFillColor(GRAY)
    c.drawString(MARGIN_L + 20, y - 44,
                 "A real website. An automated Messenger. An AI assistant. Working for you, 24/7.")

    draw_brand_footer(c, page_num, total)
    c.showPage()


def draw_system_header(c, y, eyebrow, title, tagline):
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(PURPLE)
    c.drawString(MARGIN_L, y, eyebrow)
    y -= 24

    c.setFont("Helvetica-Bold", 26)
    c.setFillColor(DARK)
    c.drawString(MARGIN_L, y, title)
    c.setFillColor(YELLOW)
    tw = c.stringWidth(title, "Helvetica-Bold", 26)
    c.rect(MARGIN_L, y - 7, tw, 4, fill=1, stroke=0)
    y -= 28

    c.setFont("Helvetica", 11)
    c.setFillColor(GRAY)
    tagline_w = W - MARGIN_L - MARGIN_R
    lines = wrap_text(c, tagline, "Helvetica", 11, tagline_w)
    for line in lines:
        c.drawString(MARGIN_L, y, line)
        y -= 16
    return y


def draw_benefit_item(c, y, num, title, desc):
    content_w = W - MARGIN_L - MARGIN_R

    # Purple numbered badge
    c.setFillColor(PURPLE)
    c.roundRect(MARGIN_L, y - 30, 34, 34, 8, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 15)
    c.setFillColor(YELLOW)
    c.drawCentredString(MARGIN_L + 17, y - 22, str(num))

    # Title
    text_x = MARGIN_L + 48
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(DARK)
    c.drawString(text_x, y - 8, title)

    # Description
    desc_y = y - 26
    desc_w = content_w - 48 - 40  # leave some space on right for checkmark
    lines = wrap_text(c, desc, "Helvetica", 10.5, desc_w)
    c.setFillColor(GRAY)
    for line in lines[:2]:
        c.setFont("Helvetica", 10.5)
        c.drawString(text_x, desc_y, line)
        desc_y -= 14

    # Yellow checkmark on the right
    check_x = W - MARGIN_R - 16
    check_y = y - 16
    c.setFillColor(YELLOW)
    c.circle(check_x, check_y, 12, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(DARK)
    c.drawCentredString(check_x, check_y - 4, "✓")

    # Divider
    c.setStrokeColor(LIGHT_GRAY)
    c.setLineWidth(0.5)
    c.line(MARGIN_L, y - 52, W - MARGIN_R, y - 52)

    return y - 62


def page_system(c, system_num, system_title, tagline, benefits, page_num, total):
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    c.setFillColor(PURPLE)
    c.rect(0, H - 8, W, 8, fill=1, stroke=0)

    y = H - 70
    y = draw_system_header(
        c, y,
        f"SYSTEM {system_num} OF 3",
        system_title,
        tagline,
    )
    y -= 14

    for num, title, desc in benefits:
        y = draw_benefit_item(c, y, num, title, desc)

    draw_brand_footer(c, page_num, total)
    c.showPage()


def page_final_cta(c, page_num, total):
    c.setFillColor(PURPLE)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    c.setFillColor(YELLOW)
    c.rect(MARGIN_L, H - 120, 60, 6, fill=1, stroke=0)

    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(YELLOW)
    c.drawString(MARGIN_L, H - 150, "READY TO GROW?")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 38)
    c.drawString(MARGIN_L, H - 210, "Stop working")
    c.drawString(MARGIN_L, H - 250, "IN your business.")
    c.setFillColor(YELLOW)
    c.drawString(MARGIN_L, H - 290, "Start growing it.")

    body_y = H - 340
    body_width = W - MARGIN_L - MARGIN_R - 40

    body = ("I help local businesses set up all 3 systems — a website that works 24/7, "
            "a Messenger bot that replies instantly, and an AI assistant trained on your business.")
    body_y = draw_wrapped(c, body, MARGIN_L, body_y, "Helvetica", 12, body_width, 18, color=white)
    body_y -= 10

    body2 = ("Done-for-you. No tech headaches. "
             "Let's talk about what would work best for your business.")
    body_y = draw_wrapped(c, body2, MARGIN_L, body_y, "Helvetica", 12, body_width, 18, color=white)
    body_y -= 28

    # Yellow CTA button
    btn_text = "Book My Free 15-Min Call  →"
    btn_w = 300
    btn_h = 52
    btn_x = MARGIN_L
    btn_y = body_y - btn_h
    c.setFillColor(YELLOW)
    c.roundRect(btn_x, btn_y, btn_w, btn_h, 26, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(DARK)
    c.drawCentredString(btn_x + btn_w / 2, btn_y + 19, btn_text)

    # Link under button
    c.setFont("Helvetica", 10)
    c.setFillColor(YELLOW)
    c.drawString(MARGIN_L, btn_y - 22, CONSULTATION_URL)

    # Closing tagline near bottom
    c.setStrokeColor(YELLOW)
    c.setLineWidth(2)
    c.line(MARGIN_L, 150, MARGIN_L + 80, 150)

    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(white)
    c.drawString(MARGIN_L, 118, "WEBDEV BY ")
    c.setFillColor(YELLOW)
    c.drawString(MARGIN_L + c.stringWidth("WEBDEV BY ", "Helvetica-Bold", 14), 118, "AJ")
    c.setFillColor(white)
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(MARGIN_L, 95, "Built to convert. Not to decorate.")

    c.showPage()


def build():
    c = canvas.Canvas(OUT, pagesize=LETTER)
    c.setTitle("Your Business, On Autopilot.")
    c.setAuthor("WEBDEV BY AJ")
    c.setSubject("Free guide — website, automated Messenger, and AI assistant for local businesses")

    system1 = [
        (1, "Customers find you 24/7",
         "Even at 3am, when your Messenger is offline and you're asleep, your website is working — answering questions and taking bookings."),
        (2, "All your info in one place",
         "Prices, menu, services, booking — no more re-explaining the same thing in every DM. Send them the link, save your time."),
        (3, "Looks more professional than a Facebook page",
         "A real website tells customers you're a serious business. It builds trust before they even message you."),
        (4, "Built-in booking — customers book themselves",
         "No more back-and-forth DMs to confirm dates, times, and details. The site does it for you, automatically."),
        (5, "Shows up on Google",
         "When someone searches 'best [your business] near me,' you want to be there. A website makes that possible."),
    ]

    system2 = [
        (1, "Replies to FAQs in seconds",
         "'Are you open?' 'How much?' 'Do you deliver?' — all answered instantly, even when you're busy or offline."),
        (2, "Works 24/7 — even at 2am",
         "A customer messaging at midnight gets a reply. They don't wait. They don't go to your competitor instead."),
        (3, "Captures leads automatically",
         "Names, phone numbers, what they want — collected and saved, ready for you to follow up when it matters."),
        (4, "Follows up with people who didn't book",
         "That customer who asked about prices and disappeared? The bot nudges them back. You get bookings you would've lost."),
        (5, "You only handle the REAL conversations",
         "The bot handles the basics. You step in only for serious inquiries — the ones actually worth your time."),
    ]

    system3 = [
        (1, "Trained on YOUR business",
         "Knows your menu, prices, services, and policies — answers just like a well-trained employee would."),
        (2, "Handles real conversations, not just scripted FAQs",
         "Understands what customers actually mean, even when they ask weird or off-script questions."),
        (3, "Works across every channel",
         "Your website, Messenger, Instagram, WhatsApp — one AI brain answering everywhere, staying consistent."),
        (4, "Speaks your customer's language",
         "Taglish, Filipino, English, or a mix — it replies naturally, however your customers actually talk."),
        (5, "Gets smarter the more it works",
         "Every conversation makes it better. It learns your business, your tone, your customers — and keeps improving."),
    ]

    page_cover(c)
    page_intro(c, 2, 6)
    page_system(c, 1, "A Website That Works While You Sleep",
                "A real website that answers questions, shows your offer, and takes bookings — all on its own.",
                system1, 3, 6)
    page_system(c, 2, "A Messenger Bot That Replies Instantly",
                "Automated replies that handle the repetitive stuff — so you stop answering the same question 50 times a day.",
                system2, 4, 6)
    page_system(c, 3, "An AI Assistant Trained on YOUR Business",
                "Not a generic chatbot. An AI that knows your business — and can actually talk to your customers.",
                system3, 5, 6)
    page_final_cta(c, 6, 6)

    c.save()
    print(f"Built: {OUT}")


if __name__ == "__main__":
    build()
