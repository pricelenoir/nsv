.PHONY: all clean

INPUTS := "Stephen Curry 2015 2016" \
          "Michael Jordan 1997 1998" \
		  "Charles Barkley 1998 1999" \
		  "Kyle Korver 2014 2015" \
		  "Grant Williams 2019 2024"

OUTPUT_DIR := shotcharts

SCRIPT := nsv.sh

all: $(OUTPUT_DIR)
	@for input in $(INPUTS); do \
		echo "Running script with input: $$input"; \
		./$(SCRIPT) $$input; \
	done

$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

clean:
	rm -rf $(OUTPUT_DIR)
