const fs = require("node:fs");
const { REST } = require("@discordjs/rest");
const { Routes } = require("discord-api-types/v9");
require("dotenv").config();

const commands = [];
const commandFiles = fs
    .readdirSync("./commands")
    .filter((file) => file.endsWith(".js"));

for (const file of commandFiles) {
    const command = require(`./commands/${file}`);
    commands.push(command.data.toJSON());
}

const rest = new REST({ version: "9" }).setToken(process.env.TOKEN);

for (i in commands)
    console.log(commands[i]),
    rest.put(
        Routes.applicationGuildCommands(
            process.env.CLIENTID,
            process.env.GUILDID
        ),
        { body: commands[i] }
    ).then(() =>
        console.log("REG STAR")
    )
    .catch(console.error);
