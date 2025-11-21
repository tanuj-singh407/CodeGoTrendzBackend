from core.utils.mail_sender import mail_sending
from core.config import get_settings
from core.database.mongodb import contact_us_data

setting = get_settings()


async def contact_us_service(name, email, phone_no, service_selected, message):


    subject = f"{name} wants to contact with you."

    html_body = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Email Template</title>

<style>
    body {{
        margin: 0;
        padding: 0;
        background: #eef1f6;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}

    .wrapper {{
        width: 100%;
        table-layout: fixed;
        background-color: #eef1f6;
        padding: 20px 0;
    }}

    .main {{
        background: #ffffff;
        width: 100%;
        max-width: 650px;
        margin: 0 auto;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }}

    .header {{
        background: linear-gradient(135deg, #4f46e5, #2563eb);
        padding: 35px 20px;
        text-align: center;
        color: #ffffff;
    }}

    .header h1 {{
        margin: 0;
        font-size: 28px;
        font-weight: 700;
        letter-spacing: 0.5px;
    }}

    .content {{
        padding: 30px;
        color: #333;
    }}

    h2 {{
        font-size: 20px;
        color: #2563eb;
        margin-bottom: 12px;
    }}

    p {{
        font-size: 15px;
        line-height: 1.6;
        margin: 6px 0;
    }}

    .label {{
        font-weight: 600;
        color: #1f3dd1;
    }}

    .box {{
        background: #f8fafc;
        border-left: 4px solid #2563eb;
        padding: 15px 18px;
        border-radius: 8px;
        margin: 10px 0 20px 0;
    }}

    .footer {{
        text-align: center;
        background: #f9fafb;
        padding: 18px 10px;
        font-size: 13px;
        color: #6b7280;
        border-top: 1px solid #e5e7eb;
    }}

    .footer a {{
        color: #2563eb;
        text-decoration: none;
    }}
</style>
</head>

<body>

<table class="wrapper" cellspacing="0" cellpadding="0">
    <tr>
        <td>

            <table class="main" cellspacing="0" cellpadding="0">
            
            <!-- Header -->
            <tr>
                <td class="header">
                    <h1>🚀 New Inquiry from CodeGoTrendz</h1>
                </td>
            </tr>

            <!-- Body Content -->
            <tr>
                <td class="content">

                    <h2>Client Details</h2>
                    <div class="box">
                        <p><span class="label">Name:</span> {name}</p>
                        <p><span class="label">Email:</span> {email}</p>
                        <p><span class="label">Phone No:</span> {phone_no}</p>
                    </div>

                    <h2>Selected Services</h2>
                    <div class="box">
                        <p>{service_selected}</p>
                    </div>

                    <h2>message</h2>
                    <div class="box">
                        <p>{message}</p>
                    </div>

                </td>
            </tr>

            <!-- Footer -->
            <tr>
                <td class="footer">
                    <p>This message was generated via <b>CodeGoTrendz Contact Form</b>.</p>
                    <p>📍 Greater Noida | 🌐 <a href="https://www.codegotrendz.com">codegotrendz.com</a></p>
                </td>
            </tr>

            </table>

        </td>
    </tr>
</table>

</body>
</html>
"""

    await mail_sending(setting.SEND_MAIL_TO, subject, html_body)

    contact_data = {
        "name": name,
        "email": email,
        "phone_no": phone_no,
        "service_selected": [service for service in service_selected],
        "message": message
    }

    response = await contact_us_data.insert_one(contact_data)

    if (response.acknowledged == True):
        return ({"msg": "Form Submitted Successfully"})