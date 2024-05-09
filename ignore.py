import noums
import timings

ignored_symbols = ['\uf068', '\uf022', '\uf048', '\uf061', '\uf073', '\uf053', '\uf064', '\uf044', '\uf066', '\uf046', '\uf075', '\uf07C', '\uf05c', '\uf075', '\uf033', '\uf038', '\uf05e', '\uf031', '\uf02f', '\uf076', '\uf027', '\uf047', '\uf043', '\uf034', '\uf04a', '\uf045', '\uf040', '\uf06e', '\uf062', '\uf067', '\uf042', '\uf070', '\uf03f', '\uf021', '\uf058', '\uf061', '\uf056', '\uf079', '\uf078', '\uf03c', '\uf023', '\uf077', '\uf020', '\uf048', '\uf046', '\uf057', '\uf030', '\uf065', '\uf064', '\uf04e', '\uf029', '\uf074', '\uf071', '\uf03e', '\uf035', '\uf044', '\uf06d', '\uf054', '\uf0d7', '\uf072', '\uf04f', '\uf068', '\uf050', '\uf032', '\uf04d', '\uf07a', '\uf07c']
ignored_symbols = list(set(ignored_symbols))
ignored_symbols = [item for item in ignored_symbols if item not in noums.noums and item not in timings.timings]