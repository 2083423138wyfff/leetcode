def train_ngd(train_x,train_y):
    eta0=0.2
    lam=0.01
    T=60
    eps=1e-10
    d=train_x.shape[1]
    w=np.zeros(d,dtype=float)
    for t in range(1,T+1):
        grad=train_x.T.dot(train_x.dot(w)-train_y)+2*lam*w
        if not np.all(np.isfinite(grad)):
            continue
        norm=np.linalg.norm(grad,2)
        if norm<eps:
            continue
        g_hat=grad/max(norm,eps)
        eta=eta0/(t**0.5)
        w=w-eta*g_hat
    return w

def predict(test_x,w):
    scores=test_x.dot(w)
    pred=(scores>=0).astype(int)

    return pred.tolist()

if __name__=="__main__":
    import numpy as np
    import sys
    import json
    s=sys.stdin.readline().strip()
    data=json.loads(s)
    train_x=np.array(data['train_X'],dtype=float)
    train_y=np.array(data["train_y"],dtype=float)
    test_x=np.array(data["test_X"],dtype=float)
    w=train_ngd(train_x,train_y)
    test_pred=predict(test_x,w)
    weights=[round(float(x),6) for x in w]
    ans={
        'weights':weights,
        'test_pred':test_pred
    }
    print(json.dumps(ans,ensure_ascii=False))

