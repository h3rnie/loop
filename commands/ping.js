const { SlashCommandBuilder } = require("@discordjs/builders");

module.exports = {
    data: new SlashCommandBuilder()
        .setName("ping")
        .setDescription("WebSocket Gateway Latency"),
    async execute(interaction) {
        const sock = interaction.client.ws;
        await interaction.reply({
            content: `Pong! ${sock.ping}ms`,
            ephemeral: true,
        });
    },
};
