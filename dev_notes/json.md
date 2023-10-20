
# JSON misk

## encode with sorted objected keys

JavaScript

```javascript
const replacer = (key, value) =>
  value instanceof Object && !(value instanceof Array)
    ? Object.keys(value)
        .sort()
        .reduce((sorted, key) => {
          sorted[key] = value[key]
          return sorted
        }, {})
    : value


// how to use
const strJson = JSON.stringify(obj, replacer)
```


CSharp

```csharp
static class SignatureHelper
{
    public static string NormalizeJsonString(string json)
    {
        JToken parsed = JToken.Parse(json);

        JToken normalized = NormalizeToken(parsed);

        return JsonConvert.SerializeObject(normalized);
    }

    private static JToken NormalizeToken(JToken token)
    {
        JObject o;
        JArray array;
        if ((o = token as JObject) != null)
        {
            List<JProperty> orderedProperties = new List<JProperty>(o.Properties());
            orderedProperties.Sort(delegate(JProperty x, JProperty y) { return x.Name.CompareTo(y.Name); });
            JObject normalized = new JObject();
            foreach (JProperty property in orderedProperties)
            {
                normalized.Add(property.Name, NormalizeToken(property.Value));
            }
            return normalized;
        }
        else if ((array = token as JArray) != null)
        {
            for (int i = 0; i < array.Count; i++)
            {
                array[i] = NormalizeToken(array[i]);
            }
            return array;
        }
        else
        {
            return token;
        }
    }
}

// how to use

    // common json encode
    strJson = JsonConvert.SerializeObject( obj);
    // sort key
    strJson = SignatureHelper.NormalizeJsonString(strJson);
```


## For number type x.0, remove the tailing .0

JavaScript

JSON.stringify already did.


CSharp

```csharp
// write a custom JsonConverter for float and write it without the trailing .0
// this is releated to Nodejs Express server issue
class FloatConverter : JsonConverter
{
    public override bool CanConvert(Type objectType) {
        return objectType == typeof(float) || objectType == typeof(double) || objectType == typeof(decimal) ;
    }

    public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)
    {
        writer.WriteRawValue( value.ToString() ) ;
    }

    public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
    {
        // return reader.Value;
        throw new NotImplementedException();
    }
}


// how to use

    var settings = new JsonSerializerSettings
    {
        Converters = new[] { new FloatConverter() }
    };

    // common json encode
    strJson = JsonConvert.SerializeObject(obj, settings);
```






