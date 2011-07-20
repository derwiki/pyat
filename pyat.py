def format(list_of_dicts, display_fields, skip_empty=True):
  """ASCII table formatting of list_of_dicts, only showing display_fields
  """
  maxlength = dict(
    (
      field,
      max(len(d[field]) for d in list_of_dicts)
    ) for field in display_fields
  )

  spacer = "+%s+\n" % "+".join('-' * maxlength[s] for s in display_fields)
  header = "|%s|\n" % "|".join(s.center(maxlength[s]) for s in display_fields)

  buffer = (spacer + header + spacer)
  for d in list_of_dicts:
    if skip_empty and not ''.join(d.values()): continue

    buffer += "|%s|\n" % "|".join(
      d[field].center(maxlength[field]) for field in display_fields
    )
  buffer += spacer
  return buffer

