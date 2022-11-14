using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using UnityEditor;
using UnityEngine;

namespace EditorUtilities.Solution
{
	public static class SyncSolutionUtilities
	{
		private static Type _syncVSType;
		private static MethodInfo _syncSolutionMethodInfo;

		private static FieldInfo _synchronizerField;
		private static object _synchronizerObject;
		private static Type _synchronizerType;
		private static MethodInfo _synchronizerSyncMethodInfo;
		
		static SyncSolutionUtilities()
		{
			_syncVSType = Type.GetType("UnityEditor.SyncVS,UnityEditor");
			_synchronizerField = _syncVSType.GetField("Synchronizer", BindingFlags.NonPublic | BindingFlags.Static);
			_syncSolutionMethodInfo = _syncVSType.GetMethod("SyncSolution", BindingFlags.Public | BindingFlags.Static);
			
			_synchronizerObject = _synchronizerField.GetValue(_syncVSType);
			_synchronizerType = _synchronizerObject.GetType();
			_synchronizerSyncMethodInfo = _synchronizerType.GetMethod("Sync", BindingFlags.Public | BindingFlags.Instance);
		}

		[MenuItem("Assets/Sync C# Solution", priority = 1000000)]
		public static void Sync()
		{
			Sync(true);
		}

		public static void Sync(bool logsEnabled)
		{
			CleanOldFiles(logsEnabled);
			Call_SyncSolution(logsEnabled);
			Call_SynchronizerSync(logsEnabled);
		}

		private static void CleanOldFiles(bool logsEnabled)
		{
			DirectoryInfo assetsDirectoryInfo = new DirectoryInfo(Application.dataPath);
			DirectoryInfo projectDirectoryInfo = assetsDirectoryInfo.Parent;

			IEnumerable<FileInfo> files = GetFilesByExtensions(projectDirectoryInfo, "*.sln", "*.csproj");
			foreach(FileInfo file in files)
			{
				if(logsEnabled)
				{
					Debug.Log($"Remove old solution file: {file.Name}");
				}
				file.Delete();
			}
		}

		private static void Call_SyncSolution(bool logsEnabled)
		{
			if(logsEnabled)
			{
				Debug.Log($"Coll method: SyncVS.Sync()");
			}

			_syncSolutionMethodInfo.Invoke(null, null);
		}

		private static void Call_SynchronizerSync(bool logsEnabled)
		{
			if(logsEnabled)
			{
				Debug.Log($"Coll method: SyncVS.Synchronizer.Sync()");
			}

			_synchronizerSyncMethodInfo.Invoke(_synchronizerObject, null);
		}

		private static IEnumerable<FileInfo> GetFilesByExtensions(DirectoryInfo dir, params string[] extensions)
		{
			extensions = extensions ?? new []{"*"};
			IEnumerable<FileInfo> files = Enumerable.Empty<FileInfo>();
			foreach(string ext in extensions)
			{
				files = files.Concat(dir.GetFiles(ext));
			}
			return files;
		}
	}
}