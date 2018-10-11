set background=dark
hi clear
if exists("syntax_on")
  syntax reset
endif
let g:colors_name = "custom"
hi Normal		guifg=cyan			guibg=black
hi Comment	term=bold		ctermfg=DarkCyan		guifg=#80a0ff
hi Constant	term=underline	ctermfg=Magenta		guifg=Magenta
hi Special	term=bold		ctermfg=DarkMagenta	guifg=Red
hi Identifier term=underline	cterm=bold			ctermfg=Cyan guifg=#40ffff
hi Statement term=bold		ctermfg=Yellow gui=bold	guifg=#aa4444
hi PreProc	term=underline	ctermfg=LightBlue	guifg=#ff80ff
hi Type	term=underline		ctermfg=LightGreen	guifg=#60ff60 gui=bold
hi Function	term=bold		ctermfg=White guifg=White
hi Repeat	term=underline	ctermfg=White		guifg=white
hi Operator				ctermfg=Red			guifg=Red
hi Ignore				ctermfg=black		guifg=bg
hi Error	term=reverse ctermbg=Red ctermfg=White guibg=Red guifg=White
hi Todo	term=standout ctermbg=Yellow ctermfg=Black guifg=Blue guibg=Yellow
hi LineNr	guifg=#90f020			ctermfg=Darkgreen cterm=none

" Common groups that link to default highlighting.
" You can specify other highlighting easily.
hi link String	Constant
hi link Character	Constant
hi link Number	Constant
hi link Boolean	Constant
hi link Float		Number
hi link Conditional	Repeat
hi link Label		Statement
hi link Keyword	Statement
hi link Exception	Statement
hi link Include	PreProc
hi link Define	PreProc
hi link Macro		PreProc
hi link PreCondit	PreProc
hi link StorageClass	Type
hi link Structure	Type
hi link Typedef	Type
hi link Tag		Special
hi link SpecialChar	Special
hi link Delimiter	Special
hi link SpecialComment Special
hi link Debug		Special

" hi Normal		guifg=#c0c0c0 guibg=#000040						ctermfg=gray ctermbg=black
" hi ErrorMsg		guifg=#ffffff guibg=#287eff						ctermfg=white ctermbg=lightblue
" hi Visual		guifg=#8080ff guibg=fg		gui=reverse				ctermfg=lightblue ctermbg=fg cterm=reverse
" hi VisualNOS	guifg=#8080ff guibg=fg		gui=reverse,underline	ctermfg=lightblue ctermbg=fg cterm=reverse,underline
" hi Todo			guifg=#d14a14 guibg=#1248d1						ctermfg=red	ctermbg=darkblue
" hi Search		guifg=#90fff0 guibg=#2050d0						ctermfg=white ctermbg=darkblue cterm=underline term=underline
" hi IncSearch	guifg=#b0ffff guibg=#2050d0							ctermfg=darkblue ctermbg=gray
" 
" hi SpecialKey		guifg=cyan			ctermfg=darkcyan
" hi Directory		guifg=cyan			ctermfg=cyan
" hi Title			guifg=magenta gui=none ctermfg=magenta cterm=bold
" hi WarningMsg		guifg=red			ctermfg=red
" hi WildMenu			guifg=yellow guibg=black ctermfg=yellow ctermbg=black cterm=none term=none
" hi ModeMsg			guifg=#22cce2		ctermfg=lightblue
" hi MoreMsg			ctermfg=darkgreen	ctermfg=darkgreen
" hi Question			guifg=green gui=none ctermfg=green cterm=none
" hi NonText			guifg=#0030ff		ctermfg=darkblue
" 
" hi StatusLine	guifg=blue guibg=darkgray gui=none		ctermfg=blue ctermbg=gray term=none cterm=none
" hi StatusLineNC	guifg=black guibg=darkgray gui=none		ctermfg=black ctermbg=gray term=none cterm=none
" hi VertSplit	guifg=black guibg=darkgray gui=none		ctermfg=black ctermbg=gray term=none cterm=none
" 
" hi Folded	guifg=#808080 guibg=#000040			ctermfg=darkgrey ctermbg=black cterm=bold term=bold
" hi FoldColumn	guifg=#808080 guibg=#000040			ctermfg=darkgrey ctermbg=black cterm=bold term=bold
" hi LineNr	guifg=#90f020			ctermfg=green cterm=none
" 
" hi DiffAdd	guibg=darkblue	ctermbg=darkblue term=none cterm=none
" hi DiffChange	guibg=darkmagenta ctermbg=magenta cterm=none
" hi DiffDelete	ctermfg=blue ctermbg=cyan gui=bold guifg=Blue guibg=DarkCyan
" hi DiffText	cterm=bold ctermbg=red gui=bold guibg=Red
" 
" hi Cursor	guifg=black guibg=yellow ctermfg=black ctermbg=yellow
" hi lCursor	guifg=black guibg=white ctermfg=black ctermbg=white
" 
" 
" hi Comment	guifg=#80a0ff ctermfg=darkred
" hi Constant	ctermfg=magenta guifg=#ffa0a0 cterm=none
" hi Special	ctermfg=brown guifg=Orange cterm=none gui=none
" hi Identifier	ctermfg=cyan guifg=#40ffff cterm=none
" hi Statement	ctermfg=yellow cterm=none guifg=#ffff60 gui=none
" hi PreProc	ctermfg=magenta guifg=#ff80ff gui=none cterm=none
" hi type		ctermfg=green guifg=#60ff60 gui=none cterm=none
" hi Underlined	cterm=underline term=underline
" hi Ignore	guifg=bg ctermfg=bg
" 
" " suggested by tigmoid, 2008 Jul 18
" hi Pmenu guifg=#c0c0c0 guibg=#404080
" hi PmenuSel guifg=#c0c0c0 guibg=#2050d0
" hi PmenuSbar guifg=blue guibg=darkgray
" hi PmenuThumb guifg=#c0c0c0
