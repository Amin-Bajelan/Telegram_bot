<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Telegram Bot README</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 2em;
      background-color: #f4f4f4;
      color: #333;
    }
    h1, h2 {
      color: #2c3e50;
    }
    code {
      background-color: #eee;
      padding: 2px 6px;
      border-radius: 4px;
    }
    pre {
      background-color: #eee;
      padding: 1em;
      border-radius: 4px;
      overflow-x: auto;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 1em;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 0.75em;
      text-align: left;
    }
    th {
      background-color: #ddd;
    }
  </style>
</head>
<body>

  <h1>🤖 Telegram Bot</h1>
  <p>This project is a simple and extendable Telegram bot built using the powerful <code>python-telegram-bot</code> library. It receives messages from users and replies automatically.</p>

  <h2>📌 Features</h2>
  <ul>
    <li>Message handling and automated replies</li>
    <li>Token stored securely in <code>config.py</code></li>
    <li>Clean file structure for easy development</li>
    <li>Ready for additional commands and upgrades</li>
  </ul>

  <h2>📁 Project Structure</h2>
  <table>
    <thead>
      <tr>
        <th>File</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>main.py</code></td>
        <td>Main script to run the bot</td>
      </tr>
      <tr>
        <td><code>config.py</code></td>
        <td>Stores Telegram Bot token</td>
      </tr>
      <tr>
        <td><code>requirements.txt</code></td>
        <td>Required Python packages</td>
      </tr>
      <tr>
        <td><code>README.md</code></td>
        <td>Project documentation</td>
      </tr>
    </tbody>
  </table>

  <h2>🚀 Getting Started</h2>
  <ol>
    <li>Clone the repository:
      <pre><code>git clone https://github.com/Amin-Bajelan/Telegram_bot.git
cd Telegram_bot</code></pre>
    </li>
    <li>Install dependencies:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Set your bot token in <code>config.py</code>:
      <pre><code>TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"</code></pre>
    </li>
    <li>Run the bot:
      <pre><code>python main.py</code></pre>
    </li>
  </ol>

  <h2>🧩 Dependencies</h2>
  <ul>
    <li><code>python-telegram-bot</code></li>
    <li><code>logging</code></li>
    <li><code>dotenv</code> (optional for secure token handling)</li>
  </ul>

  <h2>💡 Future Improvements</h2>
  <ul>
    <li>Support for commands like <code>/start</code> and <code>/help</code></li>
    <li>Connect to a database for message storage</li>
    <li>Integrate with ChatGPT for smart responses</li>
  </ul>

  <h2>👤 Developer</h2>
  <p><a href="https://github.com/Amin-Bajelan" target="_blank">Amin Bajelan</a></p>

</body>
</html>
