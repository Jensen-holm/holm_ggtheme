from plotnine import (
    theme,
    theme_classic,
    element_blank,
    element_text,
    element_line,
    scale_color_cmap,
)


def base(
    figure_size: tuple[int, int] = (10, 6),
    plot_title_size=16,
    plot_title_face="bold",
    plot_title_margin=6,
    subtitle_size=11,
    subtitle_face="plain",
    subtitle_margin=9,
    strip_text_size=12,
    strip_text_face="plain",
    caption_size=9,
    caption_face="plain",
    caption_margin=6,
    axis_text_size=9,
    axis_text_face="italic",
    axis_title_size=10,
    axis_title_face="italic",
    grid_col="#cccccc",
) -> theme:
    t = theme_classic() + theme(
        figure_size=figure_size,
        axis_line=element_blank(),
        panel_grid=element_line(color=grid_col, size=0.2),
        axis_title=element_text(size=axis_title_size, face=axis_title_face),
        axis_title_x=element_text(size=axis_title_size, face=axis_title_face),
        axis_title_y=element_text(size=axis_title_size, face=axis_text_face),
        axis_text=element_text(size=axis_text_size, face=axis_title_face),
        strip_text=element_text(hjust=0, size=strip_text_size, face=strip_text_face),
        plot_title=element_text(
            hjust=0,
            size=plot_title_size,
            face=plot_title_face,
            margin={
                "b": subtitle_margin,
                "l": plot_title_margin,
                "r": plot_title_margin,
                "t": plot_title_margin,
            },
        ),
        plot_subtitle=element_text(
            hjust=0,
            size=subtitle_size,
            margin={"b": subtitle_margin},
            face=subtitle_face,
        ),
        plot_caption=element_text(
            hjust=1, size=caption_size, margin={"t": caption_margin}, face=caption_face
        ),
        panel_grid_minor=element_line(size=0.2, color="#80808075"),
        panel_border=element_blank(),
    )
    return t


def continous(cmap: str = "jet") -> list[theme | scale_color_cmap]:
    return [base(), scale_color_cmap(cmap)]


def discrete() -> theme:
    return base()
