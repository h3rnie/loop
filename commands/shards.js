const { SlashCommandBuilder } = require("@discordjs/builders");

module.exports = {
    data: new SlashCommandBuilder()
        .setName("ping")
        .setDescription("WebSocket Shard Connection"),
    async execute(interaction) {
        const sock = interaction.client.ws;
        const ls = [
            "ready",
            "connecting",
            "disconnecting",
            "idle",
            "nearly",
            "disconnected",
            "waiting for guilds",
            "identifying",
            "resuming",
        ];
        let status = ls[sock.status];
        let no = "s";
        if (sock.shards.size == 1) {
            no = "";
        }
        await interaction.reply(
            `${sock.shards.size} shard${no} currently ${status} through ${sock.gateway}`
        );
    },
};