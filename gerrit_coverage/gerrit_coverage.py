from missing_diff_lines import missing_diff_lines
from gerrit_coverage.condense import condense

lines = missing_diff_lines()
condensed_lines = condense(lines)