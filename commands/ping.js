const { SlashCommandBuilder } = require("@discordjs/builders");

module.exports = {
    data: new SlashCommandBuilder()
        .setName("ping")
        .setDescription("WebSocket Gateway Information"),
    async execute(interaction) {
        const sock = interaction.client.ws;
        await interaction.reply(
            `Pong! ${sock.ping}ms`
        );
    },
};
