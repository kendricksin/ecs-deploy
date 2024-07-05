const express = require("express");
const bodyParser = require("body-parser");
const fs = require("fs");
const path = require("path");

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files from the 'public' directory
app.use(express.static("public"));

app.get("/", (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Customer Feedback Form</title>
    </head>
    <body>
        <h1>Customer Feedback</h1>
        <form action="/submit-feedback" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br><br>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br><br>

            <label for="feedback">Feedback:</label><br>
            <textarea id="feedback" name="feedback" rows="4" cols="50" required></textarea><br><br>

            <label for="rating">Rating:</label>
            <select id="rating" name="rating" required>
                <option value="5">5 - Excellent</option>
                <option value="4">4 - Good</option>
                <option value="3">3 - Average</option>
                <option value="2">2 - Poor</option>
                <option value="1">1 - Very Poor</option>
            </select><br><br>

            <input type="submit" value="Submit Feedback">
        </form>
    </body>
    </html>
  `);
});

app.post("/submit-feedback", (req, res) => {
  const feedback = req.body;
  const feedbackString = JSON.stringify(feedback) + "\n";

  fs.appendFile("feedback.txt", feedbackString, (err) => {
    if (err) {
      console.error("Error saving feedback:", err);
      res.status(500).send("Error saving feedback");
    } else {
      res.send("Thank you for your feedback!");
    }
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
