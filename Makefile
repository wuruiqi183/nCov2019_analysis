all: pull_data man_daily report push

pull_data:

	Rscript analysis/pull-data.R

man_daily:

	python src/demo.py

report:

	Rscript analysis/make_report.R

push:

	git add analysis/ output/ data/
	git commit -m 'update report'
	git push origin master
