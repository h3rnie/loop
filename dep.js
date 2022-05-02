const { SlashCommandBuilder } = require("@discordjs/builders");
const { REST } = require("@discordjs/rest");
const { Routes } = require("discord-api-types/v9");
require("dotenv").config();

const commands = [
    new SlashCommandBuilder()
        .setName("ping")
        .setDescription("Websocket Gateway Latency"),
    new SlashCommandBuilder()
        .setName("server")
        .setDescription("Comprehensive server information"),
    new SlashCommandBuilder()
        .setName("user")
        .setDescription("Comprehensive user information"),
].map((command) => command.toJSON());

const rest = new REST({ version: "9" }).setToken(process.env.TOKEN);

console.log("Started refreshing application (/) commands.\n");
console.log(
    Routes.applicationGuildCommands(process.env.CLIENTID, process.env.GUILDID),
    { body: commands }
);

rest.put(
    Routes.applicationGuildCommands(process.env.CLIENTID, process.env.GUILDID),
    { body: commands }
)
    .then(() => console.log("Successfully registered application commands."))
    .catch(console.error);
