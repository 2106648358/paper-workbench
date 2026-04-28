%% GB/T 7714-2015 numerical style for BibTeX
%% Based on gbt7714-2015 by https://github.com/CTeX-org/gbt7714
ENTRY { address author booktitle chapter edition editor howpublished institution journal key location month note number organization pages publisher school series title type url year doi eprint priority }
   { }
   { label extra.label sort.label short.list }

INTEGERS { output.state before.all mid.sentence after.sentence after.block after.item }

FUNCTION {init.state.consts}
{ #0 'before.all :=
  #1 'mid.sentence :=
  #2 'after.sentence :=
  #3 'after.block :=
  #4 'after.item :=
}

STRINGS { s t ref fix}

FUNCTION {output}
{ duplicate$ empty$
    'pop$
    'output.n.write
  if$
}

FUNCTION {output.n.write}
{ write$
  newline$
  "" before.all 'output.state :=
}

FUNCTION {output.check}
{ duplicate$ empty$
    { pop$ "" warning$ "'' is missing in " ref * warning$ }
    'output
  if$
}

FUNCTION {output.bibitem}
{ newline$
  "\bibitem{" write$
  label write$
  "}" write$
  newline$
  before.all 'output.state :=
}

FUNCTION {fin.entry}
{ output whitespace
  fin.sentence
  newline$
}

FUNCTION {whitespace}
{ before.all 'output.state :=
}

FUNCTION {new.block}
{ output.state before.all =
    'skip$
    'after.block 'output.state :=
  if$
}

FUNCTION {new.item}
{ after.item 'output.state :=
}

FUNCTION {not}
{ { #0 } { #1 } if$
}

FUNCTION {and}
{ 'skip$ { pop$ #0 } if$
}

FUNCTION {or}
{ { pop$ #1 } #0 if$
}

FUNCTION {init.vars}
{ "" 's :=
  "" 't :=
  #1 'mid.sentence :=
  #0 'before.all :=
}

FUNCTION {format.doi}
{ doi empty$
    { "" }
    { "doi: " doi * }
  if$
}

FUNCTION {format.title}
{ title empty$
    { "" }
    { title }
  if$
}

FUNCTION {format.author}
{ author empty$
    { "" }
    { author }
  if$
}

FUNCTION {format.institution}
{ institution empty$
    { "" }
    { institution }
  if$
}

FUNCTION {format.publisher}
{ publisher empty$
    { "" }
    { publisher }
  if$
}

FUNCTION {format.address}
{ location empty$
    { "" }
    { location }
  if$
}

FUNCTION {format.year}
{ year empty$
    { "" }
    { year }
  if$
}

FUNCTION {format.month}
{ month empty$
    { "" }
    { month }
  if$
}

FUNCTION {format.number}
{ number empty$
    { "" }
    { number }
  if$
}

FUNCTION {format.pages}
{ pages empty$
    { "" }
    { pages }
  if$
}

FUNCTION {format.volume}
{ volume empty$
    { "" }
    { volume }
  if$
}

FUNCTION {format.journal}
{ journal empty$
    { "" }
    { journal }
  if$
}

FUNCTION {n.dashify}
{ 't :=
  ""
    { t empty$ not }
    { t substring$ #1 #1 =
        { "-" *
          { t empty$ not }
          { t #1 #1 substring$ "-" = not }
          while$
        }
        { t #1 #1 substring$ *
        }
      if$
      t #2 global.max$ substring$ 't :=
    }
  while$
}

FUNCTION {word.in}
{ "" }

FUNCTION {abbreviate}
{ 't :=
  t #1 #1 substring$ "A" =
  t #1 #1 substring$ "B" =
  or
  t #1 #1 substring$ "C" =
  or
  t #1 #1 substring$ "D" =
  or
    { t #1 #3 substring$ * }
    { t }
  if$
}

FUNCTION {format.names}
{ 's := ""
  #1 't :=
  s num.names$ 't :=
  t #3 >
    { s #1 #3 substring$ * ", et al" * }
    {
      s name.format$
    }
  if$
}

FUNCTION {name.format}
{ 's :=
  #1 't :=
  s num.names$ 'fix :=
  ""
    { t #fix > }
    {
      s t "{ff }{ll}" format.name$ *
      t #fix = not
        { ", " * }
        'skip$
      if$
      t #1 + 't :=
    }
  while$
}

FUNCTION {article}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format.journal emphasize "journal" output.check
  format.year output
  "." * output
  format.number output
  "(" * output
  format.month output
  ")" * output
  ":" * output
  format.pages output
  new.item
  format.doi output
  fin.entry
}

FUNCTION {book}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format.publisher "publisher" output.check
  format.year output
  "." * output
  format.pages output
  new.item
  format.doi output
  fin.entry
}

FUNCTION {booklet}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format.address output
  format.year output
  new.item
  fin.entry
}

FUNCTION {inbook}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format.publisher "publisher" output.check
  format.year output
  "." * output
  format.pages output
  new.item
  fin.entry
}

FUNCTION {incollection}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format booktitle "booktitle" output.check
  format.publisher "publisher" output.check
  format.year output
  "." * output
  format.pages output
  new.item
  fin.entry
}

FUNCTION {inproceedings}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format.booktitle "booktitle" output.check
  format.year output
  ":" * output
  format.pages output
  new.item
  fin.entry
}

FUNCTION {conference}
{ inproceedings }

FUNCTION {manual}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format.publisher "publisher" output.check
  format.year output
  new.item
  fin.entry
}

FUNCTION {mastersthesis}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format.institution "school" output.check
  format.year output
  new.item
  fin.entry
}

FUNCTION {phdthesis}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format.institution "school" output.check
  format.year output
  new.item
  fin.entry
}

FUNCTION {misc}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format.year output
  new.item
  fin.entry
}

FUNCTION {proceedings}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format.publisher "publisher" output.check
  format.year output
  new.item
  fin.entry
}

FUNCTION {techreport}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  format.institution "institution" output.check
  format.year output
  new.item
  fin.entry
}

FUNCTION {unpublished}
{ output.bibitem
  format.author output
  author format.names "author" output.check
  new.block
  format.title show.key output
  new.block
  note "note" output.check
  format.year output
  new.item
  fin.entry
}

FUNCTION {default.type}
{ misc }

READ

SORT

EXECUTE {init.state.consts}
EXECUTE {init.vars}

ITERATE {call.type$}