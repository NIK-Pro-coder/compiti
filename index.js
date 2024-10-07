const express = require("express");
const app = express();
const { spawn } = require("child_process");

function runPythonScript(scriptPath, args, callback) {
	const pythonProcess = spawn("python", [scriptPath].concat(args));

	let data = "";
	pythonProcess.stdout.on("data", (chunk) => {
		data += chunk.toString();
	});

	pythonProcess.stderr.on("data", (error) => {
		console.error(`stderr: ${error}`);
	});

	pythonProcess.on("close", (code) => {
		if (code !== 0) {
			callback(`Error: Script exited with code ${code}`, null);
		} else {
			callback(null, data);
		}
	});
}

app.use(express.static(__dirname + "/"));
app.set("view engine", "ejs");

const router = express.Router();

app.get("/", function (req, res) {
	res.send("index.html");
});

/*
runPythonScript("scripts/backend.py", ["getClub", tag], (err, result) => {
	if (err) {
		res.status(500).send(err);
	} else {
		res.send(JSON.parse(result));
	}
});
*/

const http = require("http").createServer(app);

app.listen(3000, () => {
	console.log("Server is running on port : 3000");
});
