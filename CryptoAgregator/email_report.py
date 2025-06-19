import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIEVER
from query import query_db


def generate_html_report():
    query = """
    SELECT * FROM crypto_prices
    WHERE timestamp = (SELECT MAX(timestamp) FROM crypto_prices)
    ORDER BY change_24h_pct DESC
    """
    df = query_db(query)

    # HTML table
    html = f"""
    <html>
    <body>
        <h2>📊 Crypto Price Report - {df['timestamp'].iloc[0]}</h2>
        <table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse;">
            <tr style="background-color: #f2f2f2;">
                <th>Coin</th>
                <th>Price (USD)</th>
                <th>24h Change (%)</th>
                <th>Market Cap</th>
                <th>24h Volume</th>
            </tr>
    """
    for _, row in df.iterrows():
        html += f"""
            <tr>
                <td>{row['coin'].capitalize()}</td>
                <td>${row['price_usd']:.2f}</td>
                <td>{row['change_24h_pct']:.2f}%</td>
                <td>${row['market_cap']:,.0f}</td>
                <td>${row['volume_24h']:,.0f}</td>
            </tr>
        """
    html += """
        </table>
    </body>
    </html>
    """
    return html




def send_email_report():
    html_body = generate_html_report()

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "📈 Crypto Report (HTML)"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECIEVER

    html_part = MIMEText(html_body, "html")
    msg.attach(html_part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)

    print("✅ HTML Email sent successfully!")

