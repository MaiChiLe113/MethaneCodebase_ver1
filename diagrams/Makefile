# Build every diagram: .tex -> PDF (latexmk) -> SVG (pdftocairo).
# All rendered files land in ONE folder, diagrams/output/, named <level>_<diagram>.pdf and .svg
# (for example output/03-code_domain-model.pdf). Build byproducts go to build/ (not committed).
# Needs: a TeX Live with tikz and latexmk, and poppler-utils (pdftocairo).
#   make            build everything that changed
#   make clean      remove build/ (keeps output/)
#   make distclean  remove build/ and output/
SRC    := $(shell find 0* -name '*.tex' | sort)
NAME    = $(subst /,_,$(patsubst %.tex,%,$(1)))
PDF    := $(foreach f,$(SRC),output/$(call NAME,$(f)).pdf)
SVG    := $(PDF:.pdf=.svg)
SHARED := _common/mwstyle.tex _common/mwseq.tex

.PHONY: all clean distclean list
all: $(PDF) $(SVG)

define RULE
output/$(call NAME,$(1)).pdf: $(1) $(SHARED)
	@mkdir -p output build/$(dir $(1))
	cd $(dir $(1)) && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=$(CURDIR)/build/$(dir $(1)) $(notdir $(1)) >/dev/null
	cp build/$(patsubst %.tex,%.pdf,$(1)) $$@
endef
$(foreach f,$(SRC),$(eval $(call RULE,$(f))))

output/%.svg: output/%.pdf
	pdftocairo -svg $< $@

list:
	@printf '%s\n' $(SRC)

clean:
	rm -rf build

distclean: clean
	rm -rf output
