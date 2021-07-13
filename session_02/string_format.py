
#implicit Order


default_order = "{}, {}, {} " . format('Hari', 'Sadu', 'Naukari')
print (default_order)
# positional Order 
positional_order = "{1}, {0}, {2}" . format('Hari', 'Sadu', 'Naukari')
print (positional_order)

# keyword argument 

keyword_order = "{s}, {n}, {h} " . format(h='Hari', s='Sadu', n='Naukari')
print (keyword_order)
