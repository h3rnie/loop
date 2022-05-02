const { SlashCommandBuilder } = require("@discordjs/builders");

module.exports = {
    data: new SlashCommandBuilder()
        .setName("purge")
        .setDescription("Delete message from a specific channel.")
        .addIntegerOption((option) =>
            option
                .setName("number")
                .setDescription("Number of messages to delete.")
                .setRequired(true)
        ),
    async execute(interaction) {
        await interaction.reply({ content: `Hello`, ephemeral: true });
    },
};
