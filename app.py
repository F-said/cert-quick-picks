from shiny import App, render, reactive, ui

from code import line

app_ui = ui.page_fluid(
    ui.panel_title(
        ui.div(
            ui.h1("job-quick-picks"),
            ui.a("github", href="https://github.com/F-said/cert-quick-picks")
        )
    ),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.div("test!")
        ),
        ui.panel_main(
            ui.output_plot("line_plot")
        )
    )
)


def server(input, output, session):
    @output
    @render.plot(alt="jobs_line_plot")
    def line_plot():
        figure = line.line_stats()
        figure.show()


app = App(app_ui, server)
