
<!-- README.md is generated from README.Rmd. Please edit that file -->

# nCov2019\_analysis

<!-- badges: start -->

[![DOI](https://zenodo.org/badge/239410768.svg)](https://zenodo.org/badge/latestdoi/239410768)
[![Launch
binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JiaxiangBU/nCov2019_analysis/master)
<!-- badges: end -->

The goal of nCov2019\_analysis is to visualize the infection in Shanghai
and Guizhou province using Python and R.

I borrow from the data downloading from Lin (2020) and data manipulation
from Jian (2020).

## How to use

``` bash
make all
```

## Dependency

1.  Python 3.7.3
2.  R 3.6.0
3.  1.2.5033

## Example

See more

1.  [Shanghai infection](analysis/shanghai-ratios.md)
2.  [Guihzou infection](analysis/guizhou-ratios.md)

<img src="D:/work/nCov2019_analysis/output/shanghai-growth-rate.png" width="100%" />

<img src="D:/work/nCov2019_analysis/output/pudong-growth-rate.png" width="100%" />

## Structure

``` r
dir_tree(".")
#> .
#> +-- analysis
#> |   +-- edit-desc.Rmd
#> |   +-- guizhou-ratios.html
#> |   +-- guizhou-ratios.md
#> |   +-- guizhou-ratios.Rmd
#> |   +-- make_report.R
#> |   +-- pull-data.R
#> |   +-- pull-data.Rmd
#> |   +-- shanghai-ratios.html
#> |   +-- shanghai-ratios.md
#> |   +-- shanghai-ratios.Rmd
#> |   \-- shanghai-ratios_files
#> |       \-- figure-gfm
#> |           +-- unnamed-chunk-5-1.png
#> |           \-- unnamed-chunk-6-1.png
#> +-- data
#> |   \-- daily.csv
#> +-- DESCRIPTION
#> +-- dev_history_r_pkg.R
#> +-- dev_history_r_proj.R
#> +-- LICENSE
#> +-- LICENSE.md
#> +-- Makefile
#> +-- NAMESPACE
#> +-- nCov2019_analysis.Rproj
#> +-- NEWS.md
#> +-- output
#> |   +-- guizhou-growth-rate.png
#> |   +-- pudong-growth-rate.png
#> |   +-- qiannanzhou-growth-rate.png
#> |   \-- shanghai-growth-rate.png
#> +-- README.en.md
#> +-- README.md
#> +-- README.Rmd
#> +-- refs
#> |   \-- add.bib
#> \-- src
#>     +-- death_rate.ipynb
#>     +-- demo.html
#>     +-- demo.ipynb
#>     +-- demo.pdf
#>     +-- demo.py
#>     +-- utils.py
#>     \-- __pycache__
#>         \-- utils.cpython-37.pyc
```

## Citations

jianxu305, & Jiaxiang Li. (2020, February 12).
JiaxiangBU/nCov2019\_analysis: nCov2019\_analysis 1.0.0 (Version
v1.0.0). Zenodo. <http://doi.org/10.5281/zenodo.3665617>

``` bibtex
@software{jianxu305_2020_3665617,
  author       = {jianxu305 and
                  Jiaxiang Li},
  title        = {{JiaxiangBU/nCov2019\_analysis: nCov2019\_analysis 
                   1.0.0}},
  month        = feb,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {v1.0.0},
  doi          = {10.5281/zenodo.3665617},
  url          = {https://doi.org/10.5281/zenodo.3665617}
}
```

If you use nCov2019\_analysis, I would be very grateful if you can add a
citation in your published work. By citing nCov2019\_analysis, beyond
acknowledging the work, you contribute to make it more visible and
guarantee its growing and sustainability. For citation, please use the
BibTex or the citation content.

<h4 align="center">

**Code of Conduct**

</h4>

<h6 align="center">

Please note that the `nCov2019_analysis` project is released with a
[Contributor Code of
Conduct](https://github.com/JiaxiangBU/nCov2019_analysis/blob/master/CODE_OF_CONDUCT.md).<br>By
contributing to this project, you agree to abide by its terms.

</h6>

<h4 align="center">

**License**

</h4>

<h6 align="center">

CC0 © [Jiaxiang Li and Jian Xu and Isaac
Lin](https://github.com/JiaxiangBU/nCov2019_analysis/blob/master/LICENSE.md)

</h6>

<div id="refs" class="references">

<div id="ref-Xu2020">

Jian, Xu. 2020. GitHub. 2020.
<https://github.com/jianxu305/nCov2019_analysis>.

</div>

<div id="ref-Isaac_Lin2020">

Lin, Isaac. 2020. “DXY-Covid-19-Data: 2019新型冠状病毒疫情时间序列数据仓库 |
Covid-19/2019-nCoV Infection Time Series Data Warehouse.” GitHub. 2020.
<https://github.com/BlankerL/DXY-2019-nCoV-Data>.

</div>

</div>
