
def fib_design(fcd,Sc2,Scu2,n=11):
  """
  As per Section 31.1.2.1.2 of Model Code 2020"""
  strain = np.linspace(0,Scu2,n)
  pass

def HognestadConcreteCompressureBehaviour(fc,Sc,Scu,n=11):
  strain = np.linspace(0,Scu2,n)
  stress = np.zeros(11)
  for i,e in enumerate(strain):
    if e <= Sc:
      stress[i] = fc * ( 2*(e/Sc) - (e/Sc)**2 )
    else:
      stress[i] = fc - 0
