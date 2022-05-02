module.exports = {
    name: "interactionCreate",
    once: false,
    execute(client, interaction) {
        // DEBUG: Disable in production
        /* console.log(`${interaction.user.tag} in #${interaction.channel.name} triggered an interaction.`); */

        if (!interaction.isCommand()) return;

        const command = client.commands.get(interaction.commandName);

        if (!command) return;

        try {
            command.execute(interaction);
        } catch (error) {
            console.error(error);
            interaction.reply({
                content:
                    "Something went wrong! Try repeating the command or report this in [our support server](https://discord.gg/HmDaSEcxpA).",
                ephemeral: true,
            });
        }
    },
};
