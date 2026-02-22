using Algorithms.DataStructures;

namespace Algorithms.Tests.DataStructures;

public class UnionFindTests
{
    [Fact]
    public void Constructor_InitializesCorrectly()
    {
        var uf = new UnionFind(5);

        Assert.Equal(5, uf.Size);
        Assert.Equal(5, uf.Components);

        for (var i = 0; i < 5; i++)
        {
            Assert.Equal(i, uf.Find(i));
            Assert.Equal(1, uf.ComponentSize(i));
        }
    }

    [Fact]
    public void Union_ReducesComponentCount()
    {
        var uf = new UnionFind(5);

        uf.Union(1, 2);

        Assert.Equal(4, uf.Components);
        Assert.True(uf.Connected(1, 2));
    }

    [Fact]
    public void Union_MergesMultipleLevels()
    {
        var uf = new UnionFind(6);

        uf.Union(1, 2);
        uf.Union(2, 3);
        uf.Union(4, 5);

        Assert.True(uf.Connected(1, 3));
        Assert.False(uf.Connected(1, 4));

        Assert.Equal(3, uf.ComponentSize(1));
        Assert.Equal(2, uf.ComponentSize(4));
        Assert.Equal(3, uf.Components);
    }

    [Fact]
    public void Union_SameComponent_DoesNotChangeState()
    {
        var uf = new UnionFind(5);

        uf.Union(1, 2);
        var componentsBefore = uf.Components;

        uf.Union(1, 2); // duplicate

        Assert.Equal(componentsBefore, uf.Components);
        Assert.Equal(2, uf.ComponentSize(1));
    }

    [Fact]
    public void Find_PerformsPathCompression()
    {
        var uf = new UnionFind(6);

        uf.Union(1, 2);
        uf.Union(2, 3);
        uf.Union(3, 4);

        var rootBefore = uf.Find(4);
        var rootAfter = uf.Find(4);

        Assert.Equal(rootBefore, rootAfter);
        Assert.Equal(4, uf.ComponentSize(1));
    }

    [Fact]
    public void ComponentSize_IsCorrectAfterUnions()
    {
        var uf = new UnionFind(7);

        uf.Union(1, 2);
        uf.Union(2, 3);
        uf.Union(4, 5);

        Assert.Equal(3, uf.ComponentSize(2));
        Assert.Equal(2, uf.ComponentSize(4));
        Assert.Equal(1, uf.ComponentSize(6));
    }

    [Theory]
    [InlineData(-1)]
    [InlineData(5)]
    public void Find_InvalidIndex_Throws(int index)
    {
        var uf = new UnionFind(5);

        Assert.Throws<ArgumentOutOfRangeException>(() => uf.Find(index));
    }

    [Theory]
    [InlineData(-1)]
    [InlineData(5)]
    public void Union_InvalidIndex_Throws(int index)
    {
        var uf = new UnionFind(5);

        Assert.Throws<ArgumentOutOfRangeException>(() => uf.Union(index, 1));
    }

    [Fact]
    public void Constructor_NegativeSize_Throws()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => new UnionFind(-1));
    }
}