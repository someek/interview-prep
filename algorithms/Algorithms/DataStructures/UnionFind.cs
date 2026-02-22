namespace Algorithms.DataStructures;

public class UnionFind
{
    private readonly int[] _componentSizes;
    private readonly int[] _ids;

    public UnionFind(int size)
    {
        ArgumentOutOfRangeException.ThrowIfNegative(size);

        Size = size;
        Components = size;
        
        _componentSizes = new int[Size];
        _ids = new int[Size];

        for (var i = 0; i < size; i++)
        {
            _componentSizes[i] = 1;
            _ids[i] = i;
        }
    }

    public int Size { get; }

    public int Components { get; private set; }

    public int Find(int p)
    {
        Validate(p);
        
        var root = p;
        while (root != _ids[root])
        {
            root = _ids[root];
        }

        while (p != root)
        {
            var next = _ids[p];
            _ids[p] = root;
            p = next;
        }
        
        return root;
    }

    public bool Connected(int p, int q) => Find(p) == Find(q);
    
    public int ComponentSize(int p) => _componentSizes[Find(p)];

    public void Union(int p, int q)
    {
        Validate(p);
        Validate(q);

        if (Connected(p, q))
        {
            return;
        }
        
        var root1 = Find(p);
        var root2 = Find(q);

        if (_componentSizes[root1] < _componentSizes[root2])
        {
            _componentSizes[root2] += _componentSizes[root1];
            _ids[root1] = root2;
            _componentSizes[root1] = 0;
        }
        else
        {
            _componentSizes[root1] +=  _componentSizes[root2];
            _ids[root2] = root1;
            _componentSizes[root2] = 0;
        }

        Components -= 1;
    }

    private void Validate(int p)
    {
        ArgumentOutOfRangeException.ThrowIfNegative(p);
        ArgumentOutOfRangeException.ThrowIfGreaterThanOrEqual(p, Size);
    }
}