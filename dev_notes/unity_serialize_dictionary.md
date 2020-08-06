
# Deconde Json to somewhat Dictionary

```csharp
[Serializable] 
public class DictionaryOfStringObject : SerializableDictionary<string, object> {}

[Serializable]
public class SerializableDictionary<TKey, TValue> : Dictionary<TKey, TValue>, ISerializationCallbackReceiver
{
	[SerializeField]
	private List<TKey> keys = new List<TKey>();

	[SerializeField]
	private List<TValue> values = new List<TValue>();

	// save the dictionary to lists
	public void OnBeforeSerialize()
	{
		keys.Clear();
		values.Clear();
		foreach(KeyValuePair<TKey, TValue> pair in this)
		{
			keys.Add(pair.Key);
			values.Add(pair.Value);
		}
	}

	// load dictionary from lists
	public void OnAfterDeserialize()
	{
		this.Clear();

		if(keys.Count != values.Count)
			throw new System.Exception(string.Format("there are {0} keys and {1} values after deserialization. Make sure that both key and value types are serializable."));

		for(int i = 0; i < keys.Count; i++)
			this.Add(keys[i], values[i]);
	}
}
```

To Use...

```csharp
using System;
using UnityEngine;
using System.Collections.Generic ;

[Serializable]
public class RESP_MSG {
    public int errcode;
    public DictionaryOfStringObject data;
}

    ...
    {
        ...
        // DeSerialize
		RESP_MSG resp ;
		try {
			resp = JsonUtility.FromJson<RESP_MSG>(json_resp);
		} catch {
			Debug.Log( "json decode failed: " + json_resp ) ;
			return false ;
		}   
        ...
    }

```


